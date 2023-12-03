import torch
import re
import pickle
import time
import sys
import torch.autograd as autograd
import torch.nn as nn
import torch.optim as optim
import model
import itertools

class TBU_CutsetTi(object):
    def __init__(self, argv):
        self.text_data = sys.argv[1]
        self.datas_pkl = './model/ti_datasave.pkl'
        self.model_path = './model/NyimaTashi.pkl'
        self.save_data = sys.argv[2]
        self.device = torch.device("cpu")

    def preprocess_filekal(self):
        datas_pkl = self.datas_pkl
        text_data = self.text_data
        with open(datas_pkl, 'rb') as inp:
            word2id = pickle.load(inp)
            id2word = pickle.load(inp)
            tag2id = pickle.load(inp)
            id2tag = pickle.load(inp)
        START_TAG = "<START>"
        STOP_TAG = "<STOP>"
        EMBEDDING_DIM = 100
        HIDDEN_DIM = 200
        EPOCHS = 64
        LR = 0.005
        tag2id[START_TAG] = len(tag2id)
        x_data = []

        def save_line(line_l):
            f_w = open(self.save_data, 'a', encoding='utf-8')
            line_l = line_l.replace("+", " ")
            line_l = re.sub('་+', '་', line_l)
            line_l = re.sub('ヨ+', ' ', line_l)
            line_l = re.sub('་ ', ' ', line_l)
            line_l = re.sub('\\s+', ' ', line_l)
            line_l = line_l.strip('་')
            if line_l:
                f_w.write(line_l)
                f_w.write('\n')
            f_w.close()

        with open(text_data, 'r', encoding="utf-8") as ifp:
            wordnum = len(id2word)
            for line in ifp:
                if not line.strip():
                    save_line('\n')
                else:
                    line_last = []
                    line = line.strip()
                    replacements = {
                        'འི': '་འི',
                        'འདིར': 'འདི་ར',
                        'གྲྭར': 'གྲྭ་ར',
                        'པས': 'པ་ས',
                        'འང': '་འང',
                        'འམ': '་འམ',
                        'པོར': 'པོ་ར',
                    }
                    for old, new in replacements.items():
                        line = line.replace(old, new)
                    line = re.sub('([,.;\':\"!@#$%^&*(){}\[\]༜༝༼༽༕༖༗ྻ༘༙༚༛༆༇༃༿࿏༾༿༟༾༴,.]+)', r'ヨ\1ヨ', line)
                    line = re.sub('།+', '།', line)
                    line = line.replace('།', '་།་ ')
                    line = re.sub(r'\s+', ' ', line)
                    line = re.sub(r'(\d)(?=\d)', r'\1 ', line)
                    line = re.sub(r'(\d)(?=\D)|(\D)(?=\d)', r'\1\2 ', line)
                    line = re.sub(r'([a-zA_Z]+)|([^a-zA-Z]+)', r'\1 \2', line)
                    line = line.lstrip('།')
                    line = line.lstrip('་')
                    line = line.strip()
                    pair_nt = re.findall('[^\u0F00-\u0FFF]+', line)
                    pair_t = re.findall('[\u0F00-\u0FFF]+', line)
                    if pair_t:
                        line_last = self.preprocess_linekal(pair_nt, pair_t, line,id2word, word2id)
                        save_line(line_last)
                    else:
                        save_line(line)

    def preprocess_linekal(self, pair_nt, pair_t, line,id2word, word2id):
        a = word2id['<unk>']
        line_last = []
        if pair_nt:
            if pair_t[-1] == '' or pair_t[0] == '':
                pair_t = pair_t[:-1]
            if line[0] in ' '.join(pair_nt):
                for m in range(len(pair_t)):
                    line_x = []
                    line_s = []
                    terlit = []
                    if '་' in pair_t[m]:
                        line_s = pair_t[m].split('་')
                    else:
                        line_s.append(pair_t[m])
                    for i in range(len(line_s)):
                        if not line_s[i]: continue
                        if (line_s[i] in id2word):
                            line_x.append(word2id[line_s[i]])
                        else:
                            word2id[line_s[i]] = word2id['<unk>']
                            terlit.append(line_s[i])
                            line_x.append(word2id['<unk>'])
                    if line_x:
                        line_r = self.generate_sentencekal(line_x, id2word)
                        if m < len(pair_nt):
                            if pair_nt[m] == 'ヨ':
                                line_last.append('།')
                            else:
                                line_last.append(pair_nt[m])
                        if len(terlit) != 0:
                            c = itertools.cycle(terlit)
                            line_r = re.sub('<unk>', lambda _: next(c), line_r)
                        line_last.append(line_r)
            else:
                for m in range(len(pair_t)):
                    line_x = []
                    line_s = []
                    terlit = []
                    if '་' in pair_t[m]:
                        line_s = pair_t[m].split('་')
                    else:
                        line_s.append(pair_t[m])
                    for i in range(len(line_s)):
                        if not line_s[i]: continue
                        if (line_s[i] in id2word):
                            line_x.append(word2id[line_s[i]])
                        else:
                            word2id[line_s[i]] = word2id['<unk>']
                            terlit.append(line_s[i])
                            line_x.append(word2id['<unk>'])
                    if line_x:
                        line_r = self.generate_sentencekal(line_x, id2word)
                        if len(terlit) != 0:
                            c = itertools.cycle(terlit)
                            line_r = re.sub('<unk>', lambda _: next(c), line_r)
                        line_last.append(line_r)
                        if m < len(pair_nt):
                            if pair_nt[m] == 'ヨ':
                                line_last.append('།')
                            else:
                                line_last.append(pair_nt[m])

            line_last = ' '.join(line_last)
            return line_last
        else:
            line = line.strip()
            line_s = []
            line_x = []
            terlit = []
            if '་' in line:
                line_s = line.split('་')
            else:
                line_s.append(line)
            for i in range(len(line_s)):
                if not line_s[i]: continue
                if (line_s[i] in id2word):
                    line_x.append(word2id[line_s[i]])
                else:
                    word2id[line_s[i]] = word2id['<unk>']
                    line_x.append(word2id['<unk>'])
                    terlit.append(line_s[i])
            if line_x:
                line_last = self.generate_sentencekal(line_x, id2word)
                if len(terlit) != 0:
                    c = itertools.cycle(terlit)
                    line_last = re.sub('<unk>', lambda _: next(c), line_last)
            return line_last

    def generate_sentencekal(self, sentence, id2word):
        model = torch.load(self.model_path,map_location=torch.device('cpu'))
        word_list = [id2word[s] for s in sentence]
        sentence = torch.tensor(sentence, dtype=torch.long)
        _, predict = model.test(sentence)
        list_ = []
        for k, tag in enumerate(predict):
            if tag == 0 or tag == 1:
                list_.append(word_list[k])
                list_.append('་')
            else:
                list_.append(word_list[k])
                list_.append(' ')
        list_l = ''.join(list_)
        return list_l

if __name__ == "__main__":
    cut_sentence = TBU_CutsetTi(sys.argv)
    print('Start participle'+'\n'+'Please wait ...')
    time1 = time.time()
    cut_sentence.preprocess_filekal()
    time2 = time.time()
    print('Participle completed'+'\n'+'Total use: '+str((time2-time1))+' S')
