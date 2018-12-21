# -*- coding:utf-8 -*-
import re

# from toolsForExcel import *
from mainCode.toolsForExcel import *
import requests
import json
import time

headers = {
    "Accept-Language":"zh-CN,zh;q=0.8",
"User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0.0; zh-cn; PRA-AL00 Build/HONORPRA-AL00) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Host":"www.edu-edu.com",
"Accept-Encoding":"gzip",
"Connection": "keep-alive",
"Cookie":"JSESSIONID=A9D22FF2D797F13FFB1C2E8F24E7D979; JSESSIONID=30E3179DE363106BFCAF15821B73692E; service='http://www.edu-edu.com/sale/cas_security_check'; org.springframework.mobile.device.site.CookieSitePreferenceRepository.SITE_PREFERENCE=MOBILE; _tenant=default; JSESSIONID=8EDF39E271820A9B18F0F966D75D784B; JSESSIONID=8AC7EB6BBE0BCCDA935C47846DAF6BCC",
}

headers1 = {"User-Agent": "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; Redmi Note 4X Build/NRD90M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip",}

def get_subjectId():

    url1 = 'http://www.edu-edu.com/exam-admin/real/public/subjects/json'
    res = requests.get(url=url1,headers=headers)
    json1 = res.json()


    publi = [(item["code"],item['id'],item['name']) for item in json1["subjectMap"]["public"]]  # 获取要下载的科目列表
    majli = [(item["code"],item['id'],item['name']) for item in json1["subjectMap"]["major"]]

    print("公共课：",publi,'\n',"专业课：",majli)


def get_subjectId1():
    subjectId=[[1,'00009政治经济学（财经类）'], [4, '00020高等数学（一）'], [5, '00022高等数学（工专）'], [6, '00023高等数学（工本）'], [24, '12656毛泽东思想和中国特色社会主义理论体系概论'], [25, '03706思想道德修养与法律基础'], [26, '00012英语（一）'], [27, '00015英语（二）'], [32, '00595英语阅读（一）'], [35, '03709马克思主义基本原理概论'], [36, '03708中国近现代史纲要'], [37, '04729大学语文'], [38, '00024普通逻辑'], [39, '00051管理系统中计算机应用'], [41, '00054管理学原理'], [42, '04183概率论与数理统计（经管类）'], [43, '00420物理（工）'], [44, '00429教育学（一）'], [45, '00034社会学概论'], [46, '00037美学'], [47, '00040法学概论'], [48, '00041基础会计学'], [49, '00053对外经济管理概论'], [50, '00055企业会计学'], [67, '00244经济法概论'], [71, '04184线性代数（经管类）'], [91, '02197概率论与数理统计（二）'], [93, '02324离散数学'], [195, '00018计算机应用基础'], [230, '02198线性代数'], [7, '00043经济法概论（财经类）'], [8, '00058市场营销学'], [9, '00067财务管理学'], [10, '00070政府与事业单位会计'], [12, '00098国际市场营销学'], [13, '00107现代管理学'], [14, '00147人力资源管理（一）'], [15, '00149国际贸易理论与实务'], [16, '00150金融理论与实务'], [17, '00158资产评估'], [18, '00159高级财务会计'], [19, '00160审计学'], [22, '02331数据结构'], [23, '04741计算机网络原理'], [28, '00795综合英语（二）'], [30, '00087英语翻译'], [31, '00794综合英语（一）'], [33, '00832英语词汇学'], [34, '00596英语阅读（二）'], [40, '00228环境与资源保护法学'], [51, '00060财政学'], [52, '00065国民经济统计概论'], [53, '00093国际技术贸易'], [54, '00100国际运输与保险'], [55, '00102世界市场行情'], [56, '00144企业管理概论'], [57, '00146中国税制'], [58, '00152组织行为学'], [59, '00161财务报表分析（一）'], [60, '00182公共关系学'], [61, '00184市场营销策划'], [62, '00223中国法制史'], [63, '00226知识产权法'], [64, '00227公司法'], [65, '00230合同法'], [66, '00242民法学'], [68, '00245刑法学'], [69, '00246国际经济法概论'], [70, '00260刑事诉讼法学'], [72, '00249国际私法'], [73, '00259公证与律师制度'], [74, '00261行政法学'], [75, '00262法律文书写作'], [76, '00263外国法制史'], [77, '00264中国法律思想史'], [78, '00312政治学概论'], [79, '00319行政组织理论'], [80, '00320领导科学'], [81, '00341公文写作与处理'], [82, '00342高级语言程序设计（一）'], [83, '00522英语国家概况'], [84, '00540外国文学史'], [85, '00541语言学概论'], [87, '00603英语写作'], [88, '00604英美文学选读'], [89, '00831英语语法'], [90, '01848公务员制度'], [92, '02318计算机组成原理'], [94, '02325计算机系统结构'], [95, '02326操作系统'], [96, '03004社区护理学（一）'], [97, '03005护理教育导论'], [98, '03006护理管理学'], [99, '03007急救护理学'], [100, '03008护理学研究'], [101, '03009精神障碍护理学'], [102, '03010妇产科护理学（二）'], [103, '03011儿科护理学（二）'], [104, '03200预防医学（二）'], [105, '03201护理学导论'], [106, '03202内科护理学（二）'], [107, '03203外科护理学'], [108, '03350社会研究方法'], [109, '04435老年护理学'], [110, '04436康复护理学'], [111, '04735数据库系统原理'], [112, '04737计算机-C++程序设计（本科）'], [113, '04747Java语言程序设计（一）'], [114, '05677法理学'], [115, '05678金融法'], [116, '05680婚姻家庭法'], [117, '05844国际商务英语'], [118, '00076国际金融'], [119, '00078银行会计学'], [120, '00089国际贸易'], [121, '00090国际贸易实务（一）'], [122, '00153质量管理（一）'], [123, '00156成本会计'], [124, '00157管理会计（一）'], [125, '00162会计制度设计'], [126, '00169房地产法'], [127, '00177消费心理学'], [128, '00178市场调查与预测'], [129, '00179谈判与推销技巧'], [130, '00181广告学（一）'], [131, '00183消费经济学'], [132, '00185商品流通概论'], [133, '00186国际商务谈判'], [134, '00208国际财务管理'], [135, '00233税法'], [136, '00243民事诉讼法学'], [137, '00247国际法'], [138, '00257票据法'], [139, '00265西方法律思想史'], [140, '00292市政学'], [141, '00322中国行政史'], [142, '00394幼儿园课程'], [143, '00395科学·技术·社会'], [144, '00398学前教育原理'], [145, '00445中外教育管理史'], [146, '00449教育管理原理'], [147, '00450教育评估和督导'], [148, '00451教育经济学'], [149, '00453教育法学'], [150, '00454教育预测与规划'], [151, '00457学前教育管理'], [152, '00464中外教育简史'], [153, '00465心理卫生与心理辅导'], [154, '00466发展与教育心理学'], [155, '00467课程与教学论'], [156, '00472比较教育'], [157, '00488健康教育学'], [158, '00506写作（一）'], [159, '00529文学概论（一）'], [160, '00531中国当代文学作品选'], [161, '00534外国文学作品选'], [162, '00535现代汉语'], [163, '00644公关礼仪'], [164, '00653中国新闻事业史'], [165, '00660外国新闻事业史'], [166, '00661中外新闻作品研究'], [167, '00891国际贸易实务（三）'], [168, '00893市场信息学'], [169, '00894计算机与网络技术基础'], [170, '00896电子商务概论'], [171, '00906电子商务网站设计原理'], [172, '00910网络经济与企业管理'], [173, '00908网络营销与策划'], [174, '02113医学心理学'], [175, '02126应用文写作'], [176, '02120数据库及其应用'], [177, '00151企业经营战略'], [178, '00258保险法'], [179, '00277行政管理学'], [180, '00315当代中国政治制度'], [181, '00316西方政治制度'], [182, '00318公共政策'], [183, '00321中国文化概论'], [184, '00323西方行政学说史'], [185, '00530中国现代文学作品选'], [186, '00532中国古代文学作品选（一）'], [187, '00533中国古代文学作品选（二）'], [188, '00537中国现代文学史'], [189, '00538中国古代文学史（一）'], [190, '00539中国古代文学史（二）'], [191, '02316计算机应用技术'], [192, '04732微型计算机及接口技术'], [193, '00597英语写作基础'], [194, '02142数据结构导论'], [196, '00088基础英语'], [197, '00094外贸函电'], [199, '00096外刊经贸知识选读'], [200, '00097外贸英语写作'], [201, '00154企业管理咨询'], [202, '00163管理心理学'], [203, '00167劳动法'], [204, '00385学前卫生学'], [205, '00452教育统计与测量'], [206, '00600高级英语'], [207, '00536古代汉语'], [208, '00830现代语言学'], [209, '00833外语教学法'], [210, '00836英语科技文选'], [211, '00145生产与作业管理'], [212, '00882学前教育心理学'], [213, '00838语言与文化'], [214, '00898互联网软件应用与开发'], [215, '00900网页设计与制作'], [216, '00911互联网数据库'], [217, '00994数量方法（二）'], [218, '02141计算机网络技术'], [219, '02183机械制图（一）'], [220, '02333软件工程'], [221, '05679宪法学'], [222, '12339幼儿园教育基础'], [223, '12344学前教育政策与法规'], [224, '02159工程力学（一）'], [225, '02323操作系统概论'], [226, '00092中国对外贸易'], [227, '02185机械设计基础'], [228, '02195数控技术及应用'], [229, '02194工程经济'], [231, '02199复变函数与积分变换'], [232, '02200现代设计方法'], [233, '02202传感器与检测技术'], [234, '02205微型计算机原理与接口技术'], [235, '02238模拟、数字与电力电子技术'], [236, '02240机械工程控制基础'], [237, '02241工业用微型计算机'], [238, '02243计算机软件基础（一）'], [239, '02335网络操作系统'], [240, '02379计算机网络管理'], [241, '02382管理信息系统'], [242, '02439结构力学（二）'], [243, '02440混凝土结构设计'], [244, '02442钢结构'], [245, '02448建筑结构试验'], [246, '02628管理经济学'], [247, '02899生理学'], [248, '02901病理学'], [249, '02903药理学（一）'], [250, '02996护理伦理学'], [251, '02997护理学基础'], [252, '03000营养学'], [253, '03142互联网及其应用'], [254, '03179生物化学（三）'], [255, '03291人际关系学'], [256, '03347流体力学'], [257, '03349政府经济管理概论'], [258, '03657学前教育研究方法'], [259, '04730电子技术基础（三）'], [260, '04742通信概论'], [261, '04751计算机网络安全'], [262, '02237自动控制系统及应用'], [263, '04749网络工程'], [264, '02864微生物学与免疫学基础'], [265, '02447建筑经济与企业管理'], [266, '02404工程地质及土力学'], [267, '02275计算机基础与程序设计'], [268, '02232电工技术基础'], [269, '02236可编程控制器原理与应用'], [270, '02245机电一体化系统设计']]

    return subjectId

def get_paperId(subId):
    url = "http://www.edu-edu.com/exam-admin/real/public/exams/json/" + str(subId)

    res = requests.get(url,headers=headers1)
    jsonData = res.json()
    examidPaperName = []
    for data in jsonData["exams"]:
        examid = (data["examId"])
        titleName = data["examTitle"].replace("(","（").replace(")","）").replace("·","●")
        if re.findall(r"\d{2,4}年\d{1,2}月.*",titleName):
            yearMonth = re.findall(r"(\d{2,4})年(\d{1,2})月",titleName)
            name = re.findall(r"\d{2,4}年\d{1,2}月(.*)",titleName)[0]
            name = re.sub(r"真题.*","",name)
            # print(yearMonth[0][0])
            # print(yearMonth[0][1])

            newName = yearMonth[0][0]+"_"+yearMonth[0][1] +"_"+name
            examidPaperName.append([newName,examid])
        else:
             examidPaperName.append([titleName,examid])

    return  examidPaperName


def write_paperId():
    oldpaper = open("../paperlist2",mode="r",encoding='utf8')
    lines = oldpaper.readlines()
    # print(lines)
    # oldpaper.close()
    with open("needPaer",mode="w",encoding='utf8') as f:
        allsubid = get_subjectId1()
        for subid  in allsubid:
            name_examids = get_paperId(subid[0])
            for name_examid in name_examids:
                for line in lines:
                    if name_examid[0]+"\n" == line:
                        print("已存在==",name_examid)
                        break
                    elif name_examid[0]+"\n" != line and line==lines[-1]:
                        f.write(str(name_examid)+"\n")
                        print(str(name_examid))
                        f.flush()
                        pass
            time.sleep(2)


def any_json(paperId):
    url0 = 'http://www.edu-edu.com/exam-admin/home/my/real/exam/startNew/json/'+str(paperId)+'?site_preference=mobile&ct=client'
    res0 = requests.get(url0,headers=headers)
    print(res0.status_code)
    #
    userexam_id  = res0.json()['userExamId']

    url = 'http://www.edu-edu.com/exam-admin/home/my/real/exam/all/questions/detailsNew/json/'+str(userexam_id)+'?site_preference=mobile&ct=client'
    time.sleep(0.5)
    res = requests.get(url, headers=headers)
    dataJson = res.json()
    # print(dataJson)
    paperArry = get_paper_arry()
    print(dataJson)
    # dataJson = {'success': True, 'examId': 25, 'qTypeQs': [{'questions': [{'isRight': True, 'userAnswer': 'b', 'examTitle': '2017年4月真题及答案解析', 'answer': 'B', 'questionChoices': [{'id': 229883, 'questionId': 810, 'order': 'a', 'content': '<img src="upload/file/28698/content?__id=VNZ2rMAwiVqLaq4CuYFG.png" width="65" height="33" align="absmiddle" />', 'staticContent': '<img src="attachments/VNZ2rMAwiVqLaq4CuYFG.png" width="65" height="33" align="absmiddle" />', 'shortContent': '......'}, {'id': 229884, 'questionId': 810, 'order': 'b', 'content': '<img src="upload/file/28699/content?__id=KZX7nLuqNErVyaajniLu.png" width="71" height="31" align="absmiddle" />', 'staticContent': '<img src="attachments/KZX7nLuqNErVyaajniLu.png" width="71" height="31" align="absmiddle" />', 'shortContent': '......'}, {'id': 229885, 'questionId': 810, 'order': 'c', 'content': '<img src="upload/file/28700/content?__id=PKmKBcEibnR3dR2gtj62.png" width="70" height="27" align="absmiddle" />', 'staticContent': '<img src="attachments/PKmKBcEibnR3dR2gtj62.png" width="70" height="27" align="absmiddle" />', 'shortContent': '......'}, {'id': 229886, 'questionId': 810, 'order': 'd', 'content': '<img src="upload/file/28701/content?__id=2RLefdiBZmj9hMrucewW.png" width="74" height="36" align="absmiddle" />', 'staticContent': '<img src="attachments/2RLefdiBZmj9hMrucewW.png" width="74" height="36" align="absmiddle" />', 'shortContent': '......'}], 'hint': ' 将原点的坐标 <img src="upload/file/28702/hint?__id=3aGagxCVi3JhSAEr3V9d.png" width="44" height="27" align="absmiddle" />依次代入到各个曲线方程中去，若使方程得到满足，则原点就在该方程所表示的曲线上。只有选项B的方程得到满足。', 'baseTypeName': '单选题', 'id': 810, 'title': '<p>下列曲线中经过原点的为（ ）</p>', 'baseType': 1, 'isFavorite': False}, {'isRight': True, 'userAnswer': 'c', 'examTitle': '2017年4月真题及答案解析', 'answer': 'C', 'questionChoices': [{'id': 229887, 'questionId': 811, 'order': 'a', 'content': '<img src="upload/file/28704/content?__id=RCtDZmFrH662n7HkiXUX.png" width="72" height="51" align="absmiddle" />', 'staticContent': '<img src="attachments/RCtDZmFrH662n7HkiXUX.png" width="72" height="51" align="absmiddle" />', 'shortContent': '......'}, {'id': 229888, 'questionId': 811, 'order': 'b', 'content': '<img src="upload/file/28705/content?__id=qgsr4fBaUQeDGxRnSjCq.png" width="72" height="50" align="absmiddle" />', 'staticContent': '<img src="attachments/qgsr4fBaUQeDGxRnSjCq.png" width="72" height="50" align="absmiddle" />', 'shortContent': '......'}, {'id': 229889, 'questionId': 811, 'order': 'c', 'content': '<img src="upload/file/28706/content?__id=nfd66n7JFeaekAzi2eii.png" width="73" height="54" align="absmiddle" />', 'staticContent': '<img src="attachments/nfd66n7JFeaekAzi2eii.png" width="73" height="54" align="absmiddle" />', 'shortContent': '......'}, {'id': 229890, 'questionId': 811, 'order': 'd', 'content': '<img src="upload/file/28707/content?__id=Y4azjAMaTuvbu6UcGLXi.png" width="68" height="55" align="absmiddle" />', 'staticContent': '<img src="attachments/Y4azjAMaTuvbu6UcGLXi.png" width="68" height="55" align="absmiddle" />', 'shortContent': '......'}], 'hint': ' <img src="upload/file/28708/hint?__id=5PVhje5K7PpFHttpjRyW.png" width="480" height="49" align="absmiddle" />', 'baseTypeName': '单选题', 'id': 811, 'title': '<p> <img src="upload/file/28703/title?__id=ZmxHeArSQMZqCEsxj26D.png" width="257" height="50" align="absmiddle" /></p>', 'baseType': 1, 'isFavorite': False}, {'isRight': False, 'userAnswer': 'b', 'examTitle': '2017年4月真题及答案解析', 'answer': 'A', 'questionChoices': [{'id': 229891, 'questionId': 812, 'order': 'a', 'content': '0', 'staticContent': '0', 'shortContent': '0'}, {'id': 229892, 'questionId': 812, 'order': 'b', 'content': '1', 'staticContent': '1', 'shortContent': '1'}, {'id': 229893, 'questionId': 812, 'order': 'c', 'content': '2', 'staticContent': '2', 'shortContent': '2'}, {'id': 229894, 'questionId': 812, 'order': 'd', 'content': '3', 'staticContent': '3', 'shortContent': '3'}], 'hint': '<img src="upload/file/28710/hint?__id=S2vtCJNeaB7YRpttRUsC.png" width="422" height="50" align="absmiddle" />', 'baseTypeName': '单选题', 'id': 812, 'title': '<p><img src="upload/file/28709/title?__id=YTrbGuDzzXemUh4pKjBh.png" width="183" height="52" align="absmiddle" /></p>', 'baseType': 1, 'isFavorite': False}, {'isRight': False, 'userAnswer': 'c', 'examTitle': '2017年4月真题及答案解析', 'answer': 'D', 'questionChoices': [{'id': 229895, 'questionId': 813, 'order': 'a', 'content': '<img src="upload/file/28712/content?__id=UbUsrqiRWerAQdqJTraD.png" width="51" height="25" align="absmiddle" />', 'staticContent': '<img src="attachments/UbUsrqiRWerAQdqJTraD.png" width="51" height="25" align="absmiddle" />', 'shortContent': '......'}, {'id': 229896, 'questionId': 813, 'order': 'b', 'content': '<img src="upload/file/28713/content?__id=mkanKWbr55zvnTTharv2.png" width="40" height="25" align="absmiddle" />', 'staticContent': '<img src="attachments/mkanKWbr55zvnTTharv2.png" width="40" height="25" align="absmiddle" />', 'shortContent': '......'}, {'id': 229897, 'questionId': 813, 'order': 'c', 'content': '<img src="upload/file/28714/content?__id=B7wiPVvmGeQszZjmMPjz.png" width="37" height="27" align="absmiddle" />', 'staticContent': '<img src="attachments/B7wiPVvmGeQszZjmMPjz.png" width="37" height="27" align="absmiddle" />', 'shortContent': '......'}, {'id': 229898, 'questionId': 813, 'order': 'd', 'content': '<img src="upload/file/28715/content?__id=GAXHSDaxfyhhieEgKCRM.png" width="80" height="35" align="absmiddle" />', 'staticContent': '<img src="attachments/GAXHSDaxfyhhieEgKCRM.png" width="80" height="35" align="absmiddle" />', 'shortContent': '......'}], 'hint': '就此函数而言，其分母为0的点都是它的间断点，即 <img src="upload/file/28716/hint?__id=6hBrqFReuTixqPCcVbJb.png" width="68" height="27" align="absmiddle" />。', 'baseTypeName': '单选题', 'id': 813, 'title': '<p><img src="upload/file/28711/title?__id=rcS3wsVSqajtArea7SPk.png" width="311" height="52" align="absmiddle" /></p>', 'baseType': 1, 'isFavorite': False}, {'isRight': False, 'userAnswer': 'b', 'examTitle': '2017年4月真题及答案解析', 'answer': 'D', 'questionChoices': [{'id': 229899, 'questionId': 814, 'order': 'a', 'content': '<img src="upload/file/28718/content?__id=m5QsHi46qfwkEssHStSb.png" width="46" height="35" align="absmiddle" />', 'staticContent': '<img src="attachments/m5QsHi46qfwkEssHStSb.png" width="46" height="35" align="absmiddle" />', 'shortContent': '......'}, {'id': 229900, 'questionId': 814, 'order': 'b', 'content': '<img src="upload/file/28719/content?__id=PfShbfsUkkMwqH7aytGx.png" width="48" height="34" align="absmiddle" />', 'staticContent': '<img src="attachments/PfShbfsUkkMwqH7aytGx.png" width="48" height="34" align="absmiddle" />', 'shortContent': '......'}, {'id': 229901, 'questionId': 814, 'order': 'c', 'content': '<img src="upload/file/28720/content?__id=gbpje9bR7M6tTcEJAyQH.png" width="90" height="34" align="absmiddle" />', 'staticContent': '<img src="attachments/gbpje9bR7M6tTcEJAyQH.png" width="90" height="34" align="absmiddle" />', 'shortContent': '......'}, {'id': 229902, 'questionId': 814, 'order': 'd', 'content': '<img src="upload/file/28721/content?__id=mEfzenjpSupwqmMSvwzq.png" width="78" height="27" align="absmiddle" />', 'staticContent': '<img src="attachments/mEfzenjpSupwqmMSvwzq.png" width="78" height="27" align="absmiddle" />', 'shortContent': '......'}], 'hint': '<img src="upload/file/28722/hint?__id=cbucCNPYphQFtChMptkB.png" width="393" height="57" align="absmiddle" />', 'baseTypeName': '单选题', 'id': 814, 'title': '<p><img src="upload/file/28717/title?__id=9qB54J9Uqne7Tntbn5e9.png" width="220" height="46" align="absmiddle" /></p>', 'baseType': 1, 'isFavorite': False}, {'isRight': False, 'userAnswer': 'd', 'examTitle': '2017年4月真题及答案解析', 'answer': 'C', 'questionChoices': [{'id': 229903, 'questionId': 815, 'order': 'a', 'content': '<img src="upload/file/28724/content?__id=A44bvwccu3muAnRe3hL7.png" width="94" height="45" align="absmiddle" />', 'staticContent': '<img src="attachments/A44bvwccu3muAnRe3hL7.png" width="94" height="45" align="absmiddle" />', 'shortContent': '......'}, {'id': 229904, 'questionId': 815, 'order': 'b', 'content': '<img src="upload/file/28725/content?__id=rrSHcNvvLgAGvLzAvraq.png" width="94" height="45" align="absmiddle" />', 'staticContent': '<img src="attachments/rrSHcNvvLgAGvLzAvraq.png" width="94" height="45" align="absmiddle" />', 'shortContent': '......'}, {'id': 229905, 'questionId': 815, 'order': 'c', 'content': '<img src="upload/file/28726/content?__id=e9RQvecLCEGubRWiiSte.png" width="112" height="47" align="absmiddle" />', 'staticContent': '<img src="attachments/e9RQvecLCEGubRWiiSte.png" width="112" height="47" align="absmiddle" />', 'shortContent': '......'}, {'id': 229906, 'questionId': 815, 'order': 'd', 'content': '<img src="upload/file/28727/content?__id=tNynevmhgdXRCcCVLges.png" width="116" height="43" align="absmiddle" />', 'staticContent': '<img src="attachments/tNynevmhgdXRCcCVLges.png" width="116" height="43" align="absmiddle" />', 'shortContent': '......'}], 'hint': '<img src="upload/file/28728/hint?__id=inpYnuTF6X69YKCatwdh.png" width="446" height="57" align="absmiddle" />', 'baseTypeName': '单选题', 'id': 815, 'title': '<p><img src="upload/file/28723/title?__id=PWhgScMjsJ6NSiQwm6jF.png" width="214" height="51" align="absmiddle" /></p>', 'baseType': 1, 'isFavorite': False}, {'isRight': True, 'userAnswer': 'a', 'examTitle': '2017年4月真题及答案解析', 'answer': 'A', 'questionChoices': [{'id': 229907, 'questionId': 816, 'order': 'a', 'content': '<img src="upload/file/28730/content?__id=Wb6uhkqV4MdacamrrgCe.png" width="36" height="34" align="absmiddle" />只有极小值', 'staticContent': '<img src="attachments/Wb6uhkqV4MdacamrrgCe.png" width="36" height="34" align="absmiddle" />只有极小值', 'shortContent': '只有极小值'}, {'id': 229908, 'questionId': 816, 'order': 'b', 'content': '<img src="upload/file/28731/content?__id=4zjj7BZffLxVa7KBZ5vc.png" width="36" height="34" align="absmiddle" />只有极大值.', 'staticContent': '<img src="attachments/4zjj7BZffLxVa7KBZ5vc.png" width="36" height="34" align="absmiddle" />只有极大值.', 'shortContent': '只有极大值.'}, {'id': 229909, 'questionId': 816, 'order': 'c', 'content': '<img src="upload/file/28732/content?__id=tBnSUmTeunbFYrLYJmm7.png" width="36" height="34" align="absmiddle" />既有极小值又有极大值', 'staticContent': '<img src="attachments/tBnSUmTeunbFYrLYJmm7.png" width="36" height="34" align="absmiddle" />既有极小值又有极大值', 'shortContent': '既有极小值又有极大值'}, {'id': 229910, 'questionId': 816, 'order': 'd', 'content': '无极值', 'staticContent': '无极值', 'shortContent': '无极值'}], 'hint': '先求出 <img src="upload/file/28733/hint?__id=BePEWN3kmXE93zVpsgW2.png" width="36" height="34" align="absmiddle" />的所有极值如何再回答问题。<img src="upload/file/28734/hint?__id=sqXuXpJipHY6MvkngBfs.jpg" width="538" height="105" align="absmiddle" />', 'baseTypeName': '单选题', 'id': 816, 'title': '<p>设函数<img src="upload/file/28729/title?__id=dT7qdnJ2aHGG7yb7mW5q.png" width="145" height="44" align="absmiddle" /> ，则下列结论正确的是（ ）</p>', 'baseType': 1, 'isFavorite': False}, {'isRight': False, 'userAnswer': 'd', 'examTitle': '2017年4月真题及答案解析', 'answer': 'B', 'questionChoices': [{'id': 229911, 'questionId': 817, 'order': 'a', 'content': '<img src="upload/file/28736/content?__id=KGLcLFaciQ7QkfWihGAp.png" width="50" height="27" align="absmiddle" />', 'staticContent': '<img src="attachments/KGLcLFaciQ7QkfWihGAp.png" width="50" height="27" align="absmiddle" />', 'shortContent': '......'}, {'id': 229912, 'questionId': 817, 'order': 'b', 'content': '<img src="upload/file/28737/content?__id=fUNGDs7wWXLYcfpPthHS.png" width="38" height="33" align="absmiddle" />', 'staticContent': '<img src="attachments/fUNGDs7wWXLYcfpPthHS.png" width="38" height="33" align="absmiddle" />', 'shortContent': '......'}, {'id': 229913, 'questionId': 817, 'order': 'c', 'content': '<img src="upload/file/28738/content?__id=zhpbij5Ge6CSFgVmarJQ.png" width="50" height="32" align="absmiddle" />', 'staticContent': '<img src="attachments/zhpbij5Ge6CSFgVmarJQ.png" width="50" height="32" align="absmiddle" />', 'shortContent': '......'}, {'id': 229914, 'questionId': 817, 'order': 'd', 'content': '<img src="upload/file/28739/content?__id=Z2amYLTGryq4SZbWw3c2.png" width="40" height="29" align="absmiddle" />', 'staticContent': '<img src="attachments/Z2amYLTGryq4SZbWw3c2.png" width="40" height="29" align="absmiddle" />', 'shortContent': '......'}], 'hint': '<img src="upload/file/28740/hint?__id=HhdHgwfbwenskyPUgUST.png" width="295" height="50" align="absmiddle" />', 'baseTypeName': '单选题', 'id': 817, 'title': '<p>曲线 <img src="upload/file/28735/title?__id=6VpPDVmcdAx4fSws4sSd.png" width="70" height="54" align="absmiddle" />的铅直渐近线为（ ）</p>', 'baseType': 1, 'isFavorite': False}, {'isRight': True, 'userAnswer': 'b', 'examTitle': '2017年4月真题及答案解析', 'answer': 'B', 'questionChoices': [{'id': 229915, 'questionId': 818, 'order': 'a', 'content': '<img src="upload/file/28742/content?__id=TZytUhyQenXaBZ3fdyLP.png" width="70" height="34" align="absmiddle" />', 'staticContent': '<img src="attachments/TZytUhyQenXaBZ3fdyLP.png" width="70" height="34" align="absmiddle" />', 'shortContent': '......'}, {'id': 229916, 'questionId': 818, 'order': 'b', 'content': '<img src="upload/file/28743/content?__id=rVhEWHvnq4jaTHjurPaK.png" width="66" height="32" align="absmiddle" />', 'staticContent': '<img src="attachments/rVhEWHvnq4jaTHjurPaK.png" width="66" height="32" align="absmiddle" />', 'shortContent': '......'}, {'id': 229917, 'questionId': 818, 'order': 'c', 'content': '<img src="upload/file/28744/content?__id=qirZqcbDpFCjafBmNqQg.png" width="74" height="29" align="absmiddle" />', 'staticContent': '<img src="attachments/qirZqcbDpFCjafBmNqQg.png" width="74" height="29" align="absmiddle" />', 'shortContent': '......'}, {'id': 229918, 'questionId': 818, 'order': 'd', 'content': '<img src="upload/file/28745/content?__id=GJrDw6xPtJhtinfe6dvj.png" width="75" height="32" align="absmiddle" />', 'staticContent': '<img src="attachments/GJrDw6xPtJhtinfe6dvj.png" width="75" height="32" align="absmiddle" />', 'shortContent': '......'}], 'hint': '<img src="upload/file/28746/hint?__id=zTaHihutEKuumPfN5RQi.png" width="480" height="36" align="absmiddle" />', 'baseTypeName': '单选题', 'id': 818, 'title': '<p><img src="upload/file/28741/title?__id=YKaT3MJDSCYk4Mudvs2T.png" width="370" height="49" align="absmiddle" /></p>', 'baseType': 1, 'isFavorite': False}, {'isRight': False, 'userAnswer': 'd', 'examTitle': '2017年4月真题及答案解析', 'answer': 'A', 'questionChoices': [{'id': 229919, 'questionId': 819, 'order': 'a', 'content': '1', 'staticContent': '1', 'shortContent': '1'}, {'id': 229920, 'questionId': 819, 'order': 'b', 'content': '2', 'staticContent': '2', 'shortContent': '2'}, {'id': 229921, 'questionId': 819, 'order': 'c', 'content': '3', 'staticContent': '3', 'shortContent': '3'}, {'id': 229922, 'questionId': 819, 'order': 'd', 'content': '∞', 'staticContent': '∞', 'shortContent': '∞'}], 'hint': '直接计算<img src="upload/file/28748/hint?__id=vJSkNNuZnhbrmMAyjtRp.png" width="220" height="52" align="absmiddle" />', 'baseTypeName': '单选题', 'id': 819, 'title': '<p> <img src="upload/file/28747/title?__id=HETj4bfQLk7wmiHBnfhP.png" width="182" height="51" align="absmiddle" /></p>', 'baseType': 1, 'isFavorite': False}], 'title': '一、单项选择题（本大题共10小题，每小题3分，共30分）', 'baseType': 1}, {'questions': [{'isRight': False, 'userAnswer': 'b', 'examTitle': '2017年4月真题及答案解析', 'answer': '<img src="upload/file/28750/answer?__id=cmhzX3tseEPduw9TARvB.png" width="618" height="169" align="absmiddle" />', 'hint': '', 'baseTypeName': '问答题', 'id': 820, 'title': '<p><img src="upload/file/28749/title?__id=6uArvf6GWQHXrWKvUfyS.png" width="238" height="32" align="absmiddle" /></p>', 'baseType': 3, 'isFavorite': False}, {'isRight': False, 'userAnswer': 'b', 'examTitle': '2017年4月真题及答案解析', 'answer': '<img src="upload/file/28752/answer?__id=Lf4mbj2seRskt9EaVCXx.png" width="477" height="261" align="absmiddle" />', 'hint': '', 'baseTypeName': '问答题', 'id': 821, 'title': '<p><img src="upload/file/28751/title?__id=YZ2bTpTBupkSBdaHvjV9.png" width="144" height="63" align="absmiddle" /></p>', 'baseType': 3, 'isFavorite': False}, {'isRight': False, 'userAnswer': 'c', 'examTitle': '2017年4月真题及答案解析', 'answer': '<img src="upload/file/28754/answer?__id=kKPprAhfCTs74WGdNiie.png" width="553" height="191" align="absmiddle" />', 'hint': '', 'baseTypeName': '问答题', 'id': 822, 'title': '<p><img src="upload/file/28753/title?__id=wB5nCykzm9BT9q5CKRFi.png" width="291" height="51" align="absmiddle" /></p>', 'baseType': 3, 'isFavorite': False}, {'isRight': True, 'userAnswer': 'a', 'examTitle': '2017年4月真题及答案解析', 'answer': '<img src="upload/file/28756/answer?__id=naFTcgUYRvtzrci4Lhca.png" width="432" height="164" align="absmiddle" />', 'hint': '', 'baseTypeName': '问答题', 'id': 823, 'title': '<p><img src="upload/file/28755/title?__id=paxedrKaYqsFbrzKNbgq.png" width="156" height="51" align="absmiddle" /></p>', 'baseType': 3, 'isFavorite': False}, {'isRight': False, 'userAnswer': 'c', 'examTitle': '2017年4月真题及答案解析', 'answer': '<img src="upload/file/28758/answer?__id=cZ7tmxnuStXiBYerjiPS.png" width="412" height="261" align="absmiddle" />', 'hint': '', 'baseTypeName': '问答题', 'id': 824, 'title': '<p><img src="upload/file/28757/title?__id=An6ckvbhjXCnAZBFwPAc.png" width="331" height="58" align="absmiddle" /></p>', 'baseType': 3, 'isFavorite': False}], 'title': '二、简单计算题（本大题共5小题，每小题4分，共20分）', 'baseType': 3}, {'questions': [{'isRight': True, 'userAnswer': 'a', 'examTitle': '2017年4月真题及答案解析', 'answer': '<img src="upload/file/28760/answer?__id=QkVAAEasEGzDb7tKRZV5.png" width="582" height="166" />', 'hint': '', 'baseTypeName': '问答题', 'id': 825, 'title': '<p><img src="upload/file/28759/title?__id=uYjXegNv9gspeFiMq2tN.png" width="428" height="88" align="absmiddle" /></p>', 'baseType': 3, 'isFavorite': False}, {'isRight': False, 'userAnswer': 'c', 'examTitle': '2017年4月真题及答案解析', 'answer': '<img src="upload/file/28762/answer?__id=4r7Dy4m4FSk5dMw3y4bV.jpg" width="553" height="240" />', 'hint': '', 'baseTypeName': '问答题', 'id': 826, 'title': '<p><img src="upload/file/28761/title?__id=EQb3BkekHnAqqeKnvFjJ.png" width="297" height="50" align="absmiddle" /></p>', 'baseType': 3, 'isFavorite': False}, {'isRight': True, 'userAnswer': 'a', 'examTitle': '2017年4月真题及答案解析', 'answer': '<img src="upload/file/28764/answer?__id=VW7CQbynuGveFSZT9BVt.png" width="614" height="206" />', 'hint': '', 'baseTypeName': '问答题', 'id': 827, 'title': '<p><img src="upload/file/28763/title?__id=pZtXLcccTvpBg7fwLrg6.png" width="316" height="38" align="absmiddle" /></p>', 'baseType': 3, 'isFavorite': False}, {'isRight': False, 'userAnswer': 'c', 'examTitle': '2017年4月真题及答案解析', 'answer': '<img src="upload/file/28766/answer?__id=3GDa3TqYyn2tvUC5wmKW.png" width="558" height="236" />', 'hint': '', 'baseTypeName': '问答题', 'id': 828, 'title': '<p><img src="upload/file/28765/title?__id=pgPLhBZMQiAwGjCSggVF.png" width="277" height="32" align="absmiddle" /></p>', 'baseType': 3, 'isFavorite': False}, {'isRight': False, 'userAnswer': 'b', 'examTitle': '2017年4月真题及答案解析', 'answer': '<img src="upload/file/28768/answer?__id=y4BxgrZEd5Wwhza5LH7r.png" width="513" height="333" />', 'hint': '', 'baseTypeName': '问答题', 'id': 829, 'title': '<p><img src="upload/file/28767/title?__id=4iZCY5fruk4WuNPTnLDE.png" width="483" height="56" align="absmiddle" /></p>', 'baseType': 3, 'isFavorite': False}], 'title': '三、计算题（本大题共5小题，每小题5分，共25分）', 'baseType': 3}, {'questions': [{'isRight': False, 'userAnswer': 'c', 'examTitle': '2017年4月真题及答案解析', 'answer': '<img src="upload/file/28770/answer?__id=3mCrxFrqVf6hkfDHgq9a.png" width="615" height="395" />', 'hint': '', 'baseTypeName': '问答题', 'id': 830, 'title': '<p> （本小题6分）</p> \n<p><img src="upload/file/28769/title?__id=9thVGJbFiLmkArnYkETz.png" width="578" height="128" /></p>', 'baseType': 3, 'isFavorite': False}, {'isRight': False, 'userAnswer': 'b', 'examTitle': '2017年4月真题及答案解析', 'answer': '<img src="upload/file/28772/answer?__id=RNPh2qHAVLzU4rq4c7p2.png" width="440" height="262" />', 'hint': '', 'baseTypeName': '问答题', 'id': 831, 'title': '<p>（本小题6分）</p> \n<p><img src="upload/file/28771/title?__id=cG3XrbhuC4FrMkizCEu3.png" width="210" height="60" /></p>', 'baseType': 3, 'isFavorite': False}, {'isRight': False, 'userAnswer': 'b', 'examTitle': '2017年4月真题及答案解析', 'answer': '<img src="upload/file/28775/answer?__id=6h62rdeSAXBdAycNVWG4.png" width="414" height="220" />', 'hint': '', 'baseTypeName': '问答题', 'id': 832, 'title': '<p> （本小题6分）</p> \n<p><img src="upload/file/28773/title?__id=XsciNq7wSBEqaPxU7dva.png" width="617" height="53" align="absmiddle" />面区域．</p> \n<p><img src="upload/file/28774/title?__id=TwrKppUbR2ijLMiPR3Dq.png" width="147" height="168" /></p>', 'baseType': 3, 'isFavorite': False}, {'isRight': True, 'userAnswer': 'a', 'examTitle': '2017年4月真题及答案解析', 'answer': '<img src="upload/file/28778/answer?__id=tLktJsgvEprgnKCtqzef.png" width="569" height="324" />', 'hint': '', 'baseTypeName': '问答题', 'id': 833, 'title': '<p>（本小题7分）</p> \n<p><img src="upload/file/28776/title?__id=QT7y5C45bBQ7Q94cj7g6.png" width="469" height="138" /></p> \n<p><img src="upload/file/28777/title?__id=HC4MQqsyk7wgQGXGmz9q.png" width="210" height="184" /></p>', 'baseType': 3, 'isFavorite': False}], 'title': '四、综合题（本大题共4小题，共25分）', 'baseType': 3}]}
    startNum = 1
    for data in dataJson["qTypeQs"]:
        for dat in data["questions"]:
            oneArry = array11()
            ans = ""
            cls = dat["baseType"]

            if cls == 1 or cls == 2:  #单选
                ans = re.sub(r"[^ABCDEFabcdef]","",dat["answer"]).upper()

                for i, choice in enumerate(dat["questionChoices"]):
                    chose = re.sub('^[\. ]{0,1}[A-F][、\.． ]{0,2}?', '', choice["content"])
                    chose = re.sub(r"^\. {0,2}","",chose)
                    oneArry[i + 3] = chose
                    if "正确" in oneArry[3] and "错误" in oneArry[4]:
                        cls = 3
                        oneArry[3]= "是"
                        oneArry[4]= "不是"

            elif cls == 3:   # 问答之类的
                cls = 4
                ans = dat["answer"]
                pass
            que = re.sub(r"<[^(img)].*?>","",dat["title"]).replace("\n","")
            que = re.sub(r" {0,3}[\(（]本小题\d{1,3}分[\)）] {0,2}","",que)
            que = re.sub(r"^ {0,3}","",que)
            if not re.findall(r"^\d{1,3}世纪|^\d{2,4}年", que):
                que = re.sub(r"^\d{1,3}[\.、]", "", que)

            # que = dat["title"]
            any = ""
            if "hint" in dat.keys():
                any = dat["hint"]

            oneArry[0] = startNum
            oneArry[1] = cls
            oneArry[2] = que
            oneArry[9] = ans
            oneArry[10] = any
            print("old==",oneArry)
            oneArry = toSaveImg(oneArry,"/Users/qiu60/Desktop/zhitikuImg2/")
            print(oneArry)
            paperArry.append(oneArry)
            startNum +=1
    # print(paperArry)
    return paperArry


def test():
    arry = any_json(1132)


def run():
    myf = open("needPaer",mode="r",encoding="utf8")
    lines = myf.readlines()
    for line in lines:
        name_paperId = eval(line)
        try:
            arry = any_json(name_paperId[1])
            write_xlsx("/Users/qiu60/Desktop/智题库真题2",name_paperId[0],arry)
            print("")
            time.sleep(3)
        except Exception as e:
            print("line err",e )
            time.sleep(3)
            continue

if __name__ == '__main__':

    run()


    pass
