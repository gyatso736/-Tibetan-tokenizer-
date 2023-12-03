# - བོད་ཡིག་གི་ཚིག་མིང་དུ་དབྱེ་ཐབས། Tibetan-tokenizer 藏文分词器-
༡ བོད་ཡིག་མིང་དུ་དབྱེ་ཐབས་འདི་ནི་བོད་སྐད་ཡིག་དང་འབྲེལ་བའི་ཞིབ་འཇུག་གནང་མཁན་ཚོར་སྟོབས་བདེ་ཅུང་ཙམ་བསྐྲུན་ཆེད། བོད་ལྗོངས་སློབ་སྒྲ་ཆེན་མོའི་དགེ་རྒན་ཆེན་མོ་ཉི་མ་བཀྲ་ཤིས་ལགས་དང་ཁོང་གི་སློབ་མས་ཐབས་Bi-LSTM+CRFཟུང་འབྲེལ་བྱས་ནས་བཟོས་པ་ཞིག་ཡིན།  
༢ སྤྱོད་ཐབས་ནི།   
>>Command: **python3  NyimaTashi.py  variable༡  variable༢**  སྣོན་དགོས།  
>>དེའི་ནང་ནས། variable༡ ནི་ཁྱེད་རང་གི་མིང་དུ་དབྱེ་དགོས་པའི་ཡིག་ཆའི་ཡོང་ཁུངས་དང་variable༢ ནི་མིང་དུ་དབྱེ་བའི་འབྲས་བུ་འཇོག་ས་རེད། དེ་གཉིས་ནང་ཡིག་ཆའི་ཁུངས་ཁ་གསལ་འཇོག་དགོས་པ་ཡིན།  
>>དཔེར་ན། ཁྱེད་རང་གི་ཡིག་ཆ་ཡོང་སའི་ཁུངས་/home/ss/Desktop/file ཡིན་པ་དང་ཡིག་ཆ་མིང་དུ་དབྱ་ཟིན་རྗེས་/home/ss/Desktop/file༢ སྟེང་དུ་འཇོག་བསམ་ན་གཤམ་གསལ་ལྟར་སྣོན་དགོས།   
>>>>**python3  NyimaTashi.py  /home/ss/Desktop/file༡  /home/ss/Desktop/file༢**   

༣ ནོར་འཁྲུལ་ཡོད་ངེས་པས། ལེགས་བཅོས་ཡོངས་ཐབས་སོགས་ཀྱི་བསམ་འཆར་གང་མང་འདོན་རོགས་ཞུ། འབྲེག་གཏུག་ཡིག་ཟམ་ནི་jibudu@163.comཡིན།  
༤ བདག་དབང་སྒེར་ལ་ཡོད་པས་ཡིད་གཟབ་གནང་རོགས།
  ******
    
Version：1.0   
1、This Tibetan tokenizer based on Bi-LSTM+CRF methods, it was created with the aim of aiding researchers in the field of Tibetan natural language processing.   
2、#Usage Instructions: Execute the following command for tokenization.   
>>Command: **python3 NyimaTashi.py variable1 variable2**  
>>Where variable1 is the absolute path of the file to be tokenized, and variable2 is the absolute path of the output file for the results.  
>>For example, if the file you want to tokenize is on the desktop with the filename "1.txt," and you want the tokenized results to be output to the desktop with the filename "2.txt," the command would be:  
>>>>**python3 NyimaTashi.py ~/Desktop/1.txt ~/Desktop/2.txt**
  
3、Citation for Research Using the Tokenization System: "Research on Tibetan Word Segmentation Method Based on Bi-LSTM Combined with CRF — by Gesang Jiacuo et al."  
4、The tokenization system is developed by the team of scholars led by Professor Nyima Tashi at Tibet University, including doctoral student Gesang Jiacuo. Its purpose is to provide convenience for individuals engaged in learning and researching Tibetan information processing. Please refrain from using it for illegal purposes.  
5、Due to limitations in the corpus, there may be instances of word segmentation errors with unfamiliar words. We welcome any constructive suggestions for improvement. For inquiries, please contact us at: jibudu@163.com.  
6. All rights reserved by the team of scholars led by Professor Nyima Tashi. Legal actions will be taken against any infringement.  
   ******
     
版本：v1.0  
1、本分词系统在结合Bi-LSTM和CRF的基础上对“未登录词音节字”的识别进行了一定的改进。  
2、#使用方法：执行下面的命令进行分词。  
>>命令： **『python3 NyimaTashi.py 变量1 变量2』**  
>>其中，变量1为需要分词的文件的绝对路径，变量2为结果输出文件的绝对路径。  
>>例如：你需要分词的文件在桌面，文件名叫1.txt，分词结果也希望输出到桌面，文件名为2.txt。那么执行命令为：  
>>>>**python3 NyimaTashi.py ～/Desktop/1.txt ～/Desktop/2.txt**

3、使用本分词系统进行研究，请引用论文“基于Bi-LSTM结合CRF的藏文分词方法研究--格桑加措等”，并作出说明。  
4、本系统测试环境pytorch版本为1.12。  
5、本分词系统是由西藏大学尼玛扎西院士团队的博士生格桑加措等人开发，旨在为学习和研究藏文信息处理的人员提供便利。请勿用于非法用途。  
6、由于语料的限制，会出现生词的分词错误的情况，有好的改进方法非常欢迎大家来探讨。联系邮箱： jibudu@163.com。  
7、版权归作者所有，侵权必究。  
