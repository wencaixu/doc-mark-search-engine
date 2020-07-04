# 部分文本无意义的单词集合
STOP_WORDS = set(
    "a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,because,been,but,by,can,cannot,could,"
    "dear,did,do,does,either,else,ever,every,for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,"
    "into,is,it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,not,of,off,often,on,only,or,"
    "other,our,own,rather,said,say,says,she,should,since,so,some,than,that,the,their,them,then,there,these,they,this,"
    "tis,to,too,twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,would,yet,you,your".split(","))

# 测试使用，后期修改未文件可读
DOCUMENT_WORDS = "In order to construct our SETs of documents,we must first examine our documents for words.the " \
                 "process of extraction wrods from documents is known as parsing and tokenization;we are producing a " \
                 "set of tokens(or words) that identify the document "


