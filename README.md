# - བོད་ཡིག་གི་ཚིག་མིང་དུ་དབྱེ་བྱེད། Tibetan tokenizer 藏文分词器-
༡ བོད་ཡིག་གི་ཚིག་མིང་དུ་དབྱེ་བྱེད་འདི་ནི་བོད་སྐད་ཡིག་དང་འབྲེལ་བའི་ཞིབ་འཇུག་གནང་མཁན་ཚོར་སྟབས་བདེ་ཅུང་ཙམ་བསྐྲུན་ཆེད། བོད་ལྗོངས་སློབ་གྲྭ་ཆེན་མོའི་དགེ་རྒན་ཆེན་མོ་ཉི་མ་བཀྲ་ཤིས་ལགས་དང་ཁོང་གི་སློབ་མ་སྐལ་རྒྱ། ཀྲུང་གོ་ཤར་བྱང་སློབ་ཆེན་གྱི་རྒན་ཞའོ་ཐོང་ལགས་དང་རྒན་ཀྲུའུ་ཅིང་པའོ་ལགས། ཁོང་གཉིས་ཀྱི་སློབ་མ་བཅས་ནས་ཐབས་Bi-LSTMདང་CRFཟུང་འབྲེལ་བྱས་ནས་བཟོས་པ་ཞིག་ཡིན་ཞིང་། གཙོ་བོ་གྲངས་འབོར་ཧ་ཅང་མང་བའི་རྒྱུ་ཆ་ལ་དམིགས་ནས་བཟོས་པ་ཞིག་ཡིན།

༢ སྤྱོད་ཐབས་ནི།   
>>བསྣན་བྱ།:
>>>སྔོན་ལ། pip install -r requirments.txt སྣོན་པ་དང་།   
>>>དེ་ནས། python  NyimaTashi.py  input_file  output_file  སྣོན་དགོས།  
>>>དེའི་ནང་ནས། input_file ནི་ཁྱེད་རང་གི་མིང་དུ་དབྱེ་དགོས་པའི་ཡིག་ཆ་དང་། output_file ནི་མིང་དུ་དབྱེ་བའི་འབྲས་བུ་རེད། དེ་གཉིས་ནང་ཡིག་ཆའི་ཁུངས་ཁ་གསལ་འཇོག་དགོས་པ་ཡིན།  
>>>དཔེར་ན། ཁྱེད་རང་གི་མིང་དུ་དབྱེ་རྒྱུའི་ཡིག་ཆ་/home/ss/Desktop/file༡ ཡིན་པ་དང་ཡིག་ཆ་མིང་དུ་དབྱ་ཟིན་རྗེས་/home/ss/Desktop/file༢ ཡིན་བསམ་ན་གཤམ་གསལ་ལྟར་སྣོན་དགོས།   
>>>>pip install -r requirments.txt  
>>>>python  NyimaTashi.py /home/ss/Desktop/file༡ /home/ss/Desktop/file༢   

༣ ནོར་འཁྲུལ་ཡོད་ངེས་པས། ལེགས་བཅོས་ཡོངས་ཐབས་སོགས་ཀྱི་བསམ་འཆར་གང་མང་འདོན་རོགས་ཞུ། འབྲེག་གཏུག་ཡིག་ཟམ་ནི་jibudu@163.comཡིན།  


   ******
     
版本：v1.0  
1、本分词系统在结合Bi-LSTM和CRF的基础上对“未登录词音节字”的识别进行了一定的改进，主要针对大量的语料。  
2、#使用方法：执行下面的命令进行分词。
>>命令：首先运行 pip install -r requirments.txt 安装环境。
>>>> 其次执行 python NyimaTashi.py input_file output_file 进行分词。
>>>>> 其中，input_file为需要分词的文件的绝对路径，output_file为结果输出文件的绝对路径。  
>>例如：你需要分词的文件在桌面，文件名叫1.txt，分词结果也希望输出到桌面，文件名为2.txt。那么执行命令为：    
>>>>pip install -r requirments.txt  
>>>>python NyimaTashi.py ～/Desktop/1.txt ～/Desktop/2.txt

3、使用本分词系统进行研究，请引用论文“基于Bi-LSTM结合CRF的藏文分词方法研究--格桑加措等”，并作出说明。  
4、环境所需pytorch、python等版本可以参考requierments.txt,也可以pip install requierments.txt ་进行安装依赖包。  
5、本分词系统是由西藏大学尼玛扎西院士的团队和东北大学自然语言处理实验室肖桐教授、朱靖波教授的团队开发，旨在为学习和研究藏文信息处理的人员提供便利。请勿用于非法用途。  
6、由于语料的限制，会出现生词的分词错误的情况，有好的改进方法非常欢迎大家来探讨。联系邮箱： jibudu@163.com。  
 

  ******
    
Version：1.0   
1、This Tibetan tokenizer based on Bi-LSTM+CRF methods, it was created with the aim of aiding researchers in the field of Tibetan natural language processing.   
2、Usage Instructions: Execute the following command for tokenization.   
>>Command: 
Install all environments with command : pip install -r requirments.txt
tokenize file with command: python NyimaTashi.py input_file input_file     
>>>Where input_file is the absolute path of the file to be tokenized, and output_file is the absolute path of the output file for the results.  
>>>For example, if the file you want to tokenize is on the desktop with the filename "1.txt," and you want the tokenized results to be output to the desktop with the filename "2.txt," the command would be:      
>>>>pip install -r requirments.txt  
>>>>python NyimaTashi.py ~/Desktop/1.txt ~/Desktop/2.txt
  
3、Citation for Research Using the Tokenization System: "Research on Tibetan Word Segmentation Method Based on Bi-LSTM Combined with CRF — by Gesang Jiacuo et al."  
4、The tokenization system is developed by the team of scholars led by Professor Nyima Tashi from Tibet University and team of scholars led by Professor Tong Xiao and Professor Jingbo Zhu from NorthEasten University. Its purpose is to provide convenience for individuals engaged in learning and researching Tibetan information processing. Please refrain from using it for illegal purposes.  
5、Due to limitations in the corpus, there may be instances of word segmentation errors with unfamiliar words. We welcome any constructive suggestions for improvement. For inquiries, please contact us at: jibudu@163.com.  

致谢：
特别感谢本人导师西藏大学尼玛扎西院士、硕导赵栋材老师和东北大学自然语言处理实验室肖桐老师、朱静波老师的指导和关照，感谢东大自然语言处理实验室李银桥学长、李北学长、阿卜.杜热西提学长、景一学弟和郑童学弟等其他老师和同学的指导和关心。
