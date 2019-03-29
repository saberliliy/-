import  string
class Poetry:
    def __init__(self):
        self.filename="pre_poetry.txt"
        self.savename = "poetry.txt"
        self.poetrys=self.get_clean_poetrys()


    def  get_clean_poetrys(self):
        f=open(self.filename,"r",encoding="utf-8")
        for line in f.readlines():

            if(line.count(":")) != 1:
                continue
            title,content = line.strip('\n').strip().split(':')
            if (not content or '_' in content or '(' in content or '（' in content or "□" in content or '《' in content or '[' in content or ':' in content or '：' in content or '_' in content):
                continue
            if (not title or "（" in title or ")"in title or "。" in title):
                continue
            content = content.replace(' ', '')
            content_list = content.replace('，', '|').replace('。', '|').split('|')
            del(content_list[-1])
            if len(content_list) !=8:
                continue
            tmp=True
            for sentence in content_list:
                if len(sentence) !=5:
                    tmp=False
            if tmp==False:
                continue
            if len(title) > 8:
                continue
            title="S"+title+"E"
            w=open(self.savename,"a+",encoding="utf-8")
            w.write(title+":"+content +"\n")
            w.close()
Poetry()