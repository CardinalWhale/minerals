from django.shortcuts import render, get_object_or_404
def home(request):
    return render(request, 'vitraj/home.html')
"""
from vitraj.models import Imgminer
from vitraj.models import Chemform
from vitraj.models import Chemical
from vitraj.models import Ierchem
from vitraj.models import Ierin
from vitraj.models import Ierphy
from vitraj.models import Interface
from vitraj.models import Physic

def home(request):
    imgminer = Imgminer.objects.all()
    context = {
        'imgminer': imgminer
    }
    return render(request, 'vitraj/home.html', context)
def chemform(request):
    chemform = Chemform.objects.all()
    context = {
        'chemform': chemform
    }
    return render(request, 'vitraj/chemform.html', context)
def chemic(request):
    chemical = Chemical.objects.all()
    context = {
        'chemical': chemical
    }
    return render(request, 'vitraj/chemic.html', context)
def interface(request):
    interface = Interface.objects.all()
    context = {
        'interface': interface
    }
    return render(request, 'vitraj/interface.html', context)
def physic(request):
    physic = Physic.objects.all()
    context = {
        'physic': physic
    }
    return render(request, 'vitraj/physic.html', context)

"""

def авгит(request):
    return render(request, 'vitraj/авгит.htm')
def агат_моховой(request):
    return render(request, 'vitraj/агат_моховой.htm')
def агат(request):
    return render(request, 'vitraj/агат.htm')
def адуляр(request):
    return render(request, 'vitraj/адуляр.htm')
def азурит(request):
    return render(request, 'vitraj/азурит.htm')
def акантит(request):
    return render(request, 'vitraj/акантит.htm')
def аквамарин(request):
    return render(request, 'vitraj/аквамарин.htm')
def аксинит(request):
    return render(request, 'vitraj/аксинит.htm')
def актинолит(request):
    return render(request, 'vitraj/актинолит.htm')
def аллофан(request):
    return render(request, 'vitraj/аллофан.htm')
def алмаз(request):
    return render(request, 'vitraj/алмаз.htm')
def алтаит(request):
    return render(request, 'vitraj/алтаит.htm')
def алунит(request):
    return render(request, 'vitraj/алунит.htm')
def альбит(request):
    return render(request, 'vitraj/альбит.htm')
def альмандин(request):
    return render(request, 'vitraj/альмандин.htm')
def амазонит(request):
    return render(request, 'vitraj/амазонит.htm')
def амблигонит(request):
    return render(request, 'vitraj/амблигонит.htm')
def аметист(request):
    return render(request, 'vitraj/аметист.htm')
def амфибол_асбест(request):
    return render(request, 'vitraj/амфибол_асбест.htm')
def амфиболит(request):
    return render(request, 'vitraj/амфиболит.htm')
def анальцим(request):
    return render(request, 'vitraj/анальцим.htm')
def ангидрит(request):
    return render(request, 'vitraj/ангидрит.htm')
def англезит(request):
    return render(request, 'vitraj/англезит.htm')
def андалузит(request):
    return render(request, 'vitraj/андалузит.htm')
def андезит(request):
    return render(request, 'vitraj/андезит.htm')
def андрадит(request):
    return render(request, 'vitraj/андрадит.htm')
def анкерит(request):
    return render(request, 'vitraj/анкерит.htm')
def аннабергит(request):
    return render(request, 'vitraj/аннабергит.htm')
def анортит(request):
    return render(request, 'vitraj/анортит.htm')
def анортозит(request):
    return render(request, 'vitraj/анортозит.htm')
def антимонит(request):
    return render(request, 'vitraj/антимонит.htm')
def апатит(request):
    return render(request, 'vitraj/апатит.htm')
def апофиллит(request):
    return render(request, 'vitraj/апофиллит.htm')
def арагонит(request):
    return render(request, 'vitraj/арагонит.htm')
def аргентит(request):
    return render(request, 'vitraj/аргентит.htm')
def арфведсонит(request):
    return render(request, 'vitraj/арфведсонит.htm')
def асбест(request):
    return render(request, 'vitraj/асбест.htm')
def асболан(request):
    return render(request, 'vitraj/асболан.htm')
def астрофиллит(request):
    return render(request, 'vitraj/астрофиллит.htm')
def аурипигмент(request):
    return render(request, 'vitraj/аурипигмент.htm')
def ашарит(request):
    return render(request, 'vitraj/ашарит.htm')
def бавенит(request):
    return render(request, 'vitraj/бавенит.htm')
def бадделеит(request):
    return render(request, 'vitraj/бадделеит.htm')
def базальт(request):
    return render(request, 'vitraj/базальт.htm')
def барит(request):
    return render(request, 'vitraj/барит.htm')
def бастнезит(request):
    return render(request, 'vitraj/бастнезит.htm')
def бемит(request):
    return render(request, 'vitraj/бемит.htm')
def берилл(request):
    return render(request, 'vitraj/берилл.htm')
def бертрандит(request):
    return render(request, 'vitraj/бертрандит.htm')
def биотит(request):
    return render(request, 'vitraj/биотит.htm')
def бирюза(request):
    return render(request, 'vitraj/бирюза.htm')
def блеклая_руда(request):
    return render(request, 'vitraj/блеклая_руда.htm')
def борнит(request):
    return render(request, 'vitraj/борнит.htm')
def браунит(request):
    return render(request, 'vitraj/браунит.htm')
def бронзит(request):
    return render(request, 'vitraj/бронзит.htm')
def брошантит(request):
    return render(request, 'vitraj/брошантит.htm')
def брусит(request):
    return render(request, 'vitraj/брусит.htm')
def буланжерит(request):
    return render(request, 'vitraj/буланжерит.htm')
def бурнонит(request):
    return render(request, 'vitraj/бурнонит.htm')
def вад(request):
    return render(request, 'vitraj/вад.htm')
def ванадинит(request):
    return render(request, 'vitraj/ванадинит.htm')
def везувиан(request):
    return render(request, 'vitraj/везувиан.htm')
def вермикулит(request):
    return render(request, 'vitraj/вермикулит.htm')
def вивианит(request):
    return render(request, 'vitraj/вивианит.htm')
def висмут_самородный(request):
    return render(request, 'vitraj/висмут_самородный.htm')
def висмутин(request):
    return render(request, 'vitraj/висмутин.htm')
def витерит(request):
    return render(request, 'vitraj/витерит.htm')
def воджинит(request):
    return render(request, 'vitraj/воджинит.htm')
def волластонит(request):
    return render(request, 'vitraj/волластонит.htm')
def вольфрамит(request):
    return render(request, 'vitraj/вольфрамит.htm')
def воробьевит(request):
    return render(request, 'vitraj/воробьевит.htm')
def вульфенит(request):
    return render(request, 'vitraj/вульфенит.htm')
def вюртцит(request):
    return render(request, 'vitraj/вюртцит.htm')
def габбро(request):
    return render(request, 'vitraj/габбро.htm')
def галенит(request):    
    return render(request, 'vitraj/галенит.htm')
def галит(request):
    return render(request, 'vitraj/галит.htm')
def галлуазит(request):
    return render(request, 'vitraj/галлуазит.htm')
def гарниерит(request):
    return render(request, 'vitraj/гарниерит.htm')
def гарцбургит(request):
    return render(request, 'vitraj/гарцбургит.htm')
def гаусманит(request):
    return render(request, 'vitraj/гаусманит.htm')
def геденбергит(request):
    return render(request, 'vitraj/геденбергит.htm')
def гейландит(request):
    return render(request, 'vitraj/гейландит.htm')
def гельвин(request):
    return render(request, 'vitraj/гельвин.htm')
def гематит(request):
    return render(request, 'vitraj/гематит.htm')
def гемиморфит(request):
    return render(request, 'vitraj/гемиморфит.htm')
def гетит(request):
    return render(request, 'vitraj/гетит.htm')
def гиацинт(request):
    return render(request, 'vitraj/гиацинт.htm')
def гидраргиллит(request):
    return render(request, 'vitraj/гидраргиллит.htm')
def гидроборацит(request):
    return render(request, 'vitraj/гидроборацит.htm')
def гиперстен(request):
    return render(request, 'vitraj/гиперстен.htm')
def гипс(request):
    return render(request, 'vitraj/гипс.htm')
def глауберит(request):
    return render(request, 'vitraj/глауберит.htm')
def глауконит(request):
    return render(request, 'vitraj/глауконит.htm')
def глаукофан(request):
    return render(request, 'vitraj/глаукофан.htm')
def гнейс(request):
    return render(request, 'vitraj/гнейс.htm')
def гранат(request):
    return render(request, 'vitraj/гранат.htm')
def гранит_порфир(request):
    return render(request, 'vitraj/гранит_порфир.htm')
def гранит_рапакиви(request):
    return render(request, 'vitraj/гранит_рапакиви.htm')
def гранит(request):
    return render(request, 'vitraj/гранит.htm')
def гранодиорит(request):
    return render(request, 'vitraj/гранодиорит.htm')
def графит(request):
    return render(request, 'vitraj/графит.htm')
def гроссуляр(request):
    return render(request, 'vitraj/гроссуляр.htm')
def даналит(request):
    return render(request, 'vitraj/даналит.htm')
def датолит(request):
    return render(request, 'vitraj/датолит.htm')
def дацит(request):
    return render(request, 'vitraj/дацит.htm')
def джемсонит(request):
    return render(request, 'vitraj/джемсонит.htm')
def диаспор(request):
    return render(request, 'vitraj/диаспор.htm')
def диккит(request):
    return render(request, 'vitraj/диккит.htm')
def диопсид(request):
    return render(request, 'vitraj/диопсид.htm')
def диоптаз(request):
    return render(request, 'vitraj/диоптаз.htm')
def диорит_порфирит(request):
    return render(request, 'vitraj/диорит_порфирит.htm')
def диорит(request):
    return render(request, 'vitraj/диорит.htm')
def долерит(request):
    return render(request, 'vitraj/долерит.htm')
def доломит(request):
    return render(request, 'vitraj/доломит.htm')
def жадеит(request):
    return render(request, 'vitraj/жадеит.htm')
def железо_самородное(request):
    return render(request, 'vitraj/железо_самородное.htm')
def золото_самородное(request):
    return render(request, 'vitraj/золото_самородное.htm')
def изумруд(request):
    return render(request, 'vitraj/изумруд.htm')
def ильваит(request):
    return render(request, 'vitraj/ильваит.htm')
def ильменит(request):
    return render(request, 'vitraj/ильменит.htm')
def ильменорутил(request):
    return render(request, 'vitraj/ильменорутил.htm')
def иодаргирит(request):
    return render(request, 'vitraj/иодаргирит.htm')
def исландский_шпат(request):
    return render(request, 'vitraj/исландский_шпат.htm')
def каинит(request):
    return render(request, 'vitraj/каинит.htm')
def калаверит(request):
    return render(request, 'vitraj/калаверит.htm')
def калиевая_селитра(request):
    return render(request, 'vitraj/калиевая_селитра.htm')
def кальцит(request):
    return render(request, 'vitraj/кальцит.htm')
def канкринит(request):
    return render(request, 'vitraj/канкринит.htm')
def карбонатит(request):
    return render(request, 'vitraj/карбонатит.htm')
def карналлит(request):
    return render(request, 'vitraj/карналлит.htm')
def карнотит(request):
    return render(request, 'vitraj/карнотит.htm')
def касситерит(request):
    return render(request, 'vitraj/касситерит.htm')
def кварц(request):
    return render(request, 'vitraj/кварц.htm')
def кварцит(request):
    return render(request, 'vitraj/кварцит.htm')
def квасцы_природные(request):
    return render(request, 'vitraj/квасцы_природные.htm')
def кераргирит(request):
    return render(request, 'vitraj/кераргирит.htm')
def кианит(request):
    return render(request, 'vitraj/кианит.htm')
def киноварь(request):
    return render(request, 'vitraj/киноварь.htm')
def кнопит(request):
    return render(request, 'vitraj/кнопит.htm')
def кобальтин(request):
    return render(request, 'vitraj/кобальтин.htm')
def ковеллин(request):
    return render(request, 'vitraj/ковеллин.htm')
def колеманит(request):
    return render(request, 'vitraj/колеманит.htm')
def колумбит(request):
    return render(request, 'vitraj/колумбит.htm')
def кордиерит(request):
    return render(request, 'vitraj/кордиерит.htm')
def корунд(request):
    return render(request, 'vitraj/корунд.htm')
def кремень(request):
    return render(request, 'vitraj/кремень.htm')
def криолит(request):
    return render(request, 'vitraj/криолит.htm')
def кристаллический_сланец(request):
    return render(request, 'vitraj/кристаллический_сланец.htm')
def крокоит(request):
    return render(request, 'vitraj/крокоит.htm')
def ксенотим(request):
    return render(request, 'vitraj/ксенотим.htm')
def кубанит(request):
    return render(request, 'vitraj/кубанит.htm')
def куприт(request):
    return render(request, 'vitraj/куприт.htm')
def лабрадор(request):
    return render(request, 'vitraj/лабрадор.htm')
def лазурит(request):
    return render(request, 'vitraj/лазурит.htm')
def лампрофиллит(request):
    return render(request, 'vitraj/лампрофиллит.htm')
def лейцит(request):
    return render(request, 'vitraj/лейцит.htm')
def лепидокрокит(request):
    return render(request, 'vitraj/лепидокрокит.htm')
def лепидолит (request):
    return render(request, 'vitraj/лепидолит.htm')
def лерцолит(request):
    return render(request, 'vitraj/лерцолит.htm')
def липарит(request):
    return render(request, 'vitraj/липарит.htm')
def ловчоррит(request):
    return render(request, 'vitraj/ловчоррит.htm')
def лопарит(request):
    return render(request, 'vitraj/лопарит.htm')
def магнезит(request):
    return render(request, 'vitraj/магнезит.htm')
def магнетит(request):
    return render(request, 'vitraj/магнетит.htm')
def малахит(request):
    return render(request, 'vitraj/малахит.htm')
def манганит(request):
    return render(request, 'vitraj/манганит.htm')
def маргарит(request):
    return render(request, 'vitraj/маргарит.htm')
def марказит(request):
    return render(request, 'vitraj/марказит.htm')
def марматит(request):
    return render(request, 'vitraj/марматит.htm')
def медь_самородная(request):
    return render(request, 'vitraj/медь_самородная.htm')
def метациннабарит(request):
    return render(request, 'vitraj/метациннабарит.htm')
def микроклин(request):
    return render(request, 'vitraj/микроклин.htm')
def миларит(request):
    return render(request, 'vitraj/миларит.htm')
def миллерит(request):
    return render(request, 'vitraj/миллерит.htm')
def мирабилит(request):
    return render(request, 'vitraj/мирабилит.htm')
def молибденит(request):
    return render(request, 'vitraj/молибденит.htm')
def монацит(request):
    return render(request, 'vitraj/монацит.htm')
def монцонит_порфир(request):
    return render(request, 'vitraj/монцонит_порфир.htm')
def мрамор(request):
    return render(request, 'vitraj/мрамор.htm')
def мусковит(request):
    return render(request, 'vitraj/мусковит.htm')
def мышьяк_самородный(request):
    return render(request, 'vitraj/мышьяк_самородный.htm')
def натролит(request):
    return render(request, 'vitraj/натролит.htm')
def нефелин(request):
    return render(request, 'vitraj/нефелин.htm')
def нефелиновый_сиенит(request):
    return render(request, 'vitraj/нефелиновый_сиенит.htm')
def нефелиновый_фонолит(request):
    return render(request, 'vitraj/нефелиновый_фонолит.htm')
def нефрит(request):
    return render(request, 'vitraj/нефрит.htm')
def никелин(request):
    return render(request, 'vitraj/никелин.htm')
def обсидиан(request):
    return render(request, 'vitraj/обсидиан.htm')
def оливин(request):
    return render(request, 'vitraj/оливин.htm')
def олигоклаз(request):
    return render(request, 'vitraj/олигоклаз.htm')
def оловянное_дерево(request):
    return render(request, 'vitraj/оловянное_дерево.htm')
def оникс(request):
    return render(request, 'vitraj/оникс.htm')
def опал(request):
    return render(request, 'vitraj/опал.htm')
def ортит(request):
    return render(request, 'vitraj/ортит.htm')
def ортоклаз(request):
    return render(request, 'vitraj/ортоклаз.htm')
def паризит(request):
    return render(request, 'vitraj/паризит.htm')
def пегматит(request):
    return render(request, 'vitraj/пегматит.htm')
def перидотит(request):
    return render(request, 'vitraj/перидотит.htm')
def перовскит(request):
    return render(request, 'vitraj/перовскит.htm')
def песчаник(request):
    return render(request, 'vitraj/песчаник.htm')
def петалит(request):
    return render(request, 'vitraj/петалит.htm')
def пираргирит(request):
    return render(request, 'vitraj/пираргирит.htm')
def пирит(request):
    return render(request, 'vitraj/пирит.htm')
def пиролюзит(request):
    return render(request, 'vitraj/пиролюзит.htm')
def пироморфит(request):
    return render(request, 'vitraj/пироморфит.htm')
def пирофиллит(request):
    return render(request, 'vitraj/пирофиллит.htm')
def пирохлор(request):
    return render(request, 'vitraj/пирохлор.htm')
def пирротин(request):
    return render(request, 'vitraj/пирротин.htm')
def повеллит(request):
    return render(request, 'vitraj/повеллит.htm')
def полигалит(request):
    return render(request, 'vitraj/полигалит.htm')
def поллуцит(request):
    return render(request, 'vitraj/поллуцит.htm')
def пренит(request):
    return render(request, 'vitraj/пренит.htm')
def прустит(request):
    return render(request, 'vitraj/прустит.htm')
def псиломелан(request):
    return render(request, 'vitraj/псиломелан.htm')
def реальгар(request):
    return render(request, 'vitraj/реальгар.htm')
def рибекит(request):
    return render(request, 'vitraj/рибекит.htm')
def риолит(request):
    return render(request, 'vitraj/риолит.htm')
def роговая_обманка(request):
    return render(request, 'vitraj/роговая_обманка.htm')
def родонит(request):    
    return render(request, 'vitraj/родонит.htm')
def родохрозит(request):
    return render(request, 'vitraj/родохрозит.htm')
def ростерит(request):
    return render(request, 'vitraj/ростерит.htm')
def рубин(request):
    return render(request, 'vitraj/рубин.htm')
def рутил(request):
    return render(request, 'vitraj/рутил.htm')
def самарскит(request):
    return render(request, 'vitraj/самарскит.htm')
def санидин(request):
    return render(request, 'vitraj/санидин.htm')
def селенит(request):
    return render(request, 'vitraj/селенит.htm')
def сера_самородная(request):
    return render(request, 'vitraj/сера_самородная.htm')
def сердолик(request):
    return render(request, 'vitraj/сердолик.htm')
def серпентин(request):
    return render(request, 'vitraj/серпентин.htm')
def серпентинит(request):
    return render(request, 'vitraj/серпентинит.htm')
def сидерит(request):
    return render(request, 'vitraj/сидерит.htm')
def сиенит(request):
    return render(request, 'vitraj/сиенит.htm')
def силлиманит(request):
    return render(request, 'vitraj/силлиманит.htm')
def сильвин(request):
    return render(request, 'vitraj/сильвин.htm')
def скаполит(request):
    return render(request, 'vitraj/скаполит.htm')
def сколацит(request):
    return render(request, 'vitraj/сколацит.htm')
def скуттерудит(request):
    return render(request, 'vitraj/скуттерудит.htm')
def сланец(request):
    return render(request, 'vitraj/сланец.htm')
def слюдяной_сланец(request):
    return render(request, 'vitraj/слюдяной_сланец.htm')
def смитсонит(request):
    return render(request, 'vitraj/смитсонит.htm')
def содалит(request):
    return render(request, 'vitraj/содалит.htm')
def станнин(request):
    return render(request, 'vitraj/станнин.htm')
def стеллерит(request):
    return render(request, 'vitraj/стеллерит.htm')
def стильбит(request):
    return render(request, 'vitraj/стильбит.htm')
def стронцианит(request):
    return render(request, 'vitraj/стронцианит.htm')
def сурьма_самородная(request):
    return render(request, 'vitraj/сурьма_самородная.htm')
def сфалерит(request):
    return render(request, 'vitraj/сфалерит.htm')
def тальк(request):
    return render(request, 'vitraj/тальк.htm')
def тенардит(request):
    return render(request, 'vitraj/тенардит.htm')
def теннантит(request):
    return render(request, 'vitraj/теннантит.htm')
def тенорит(request):
    return render(request, 'vitraj/тенорит.htm')
def тетраэдрит(request):
    return render(request, 'vitraj/тетраэдрит.htm')
def тингуаит(request):
    return render(request, 'vitraj/тингуаит.htm')
def титанит(request):
    return render(request, 'vitraj/титанит.htm')
def топаз(request):
    return render(request, 'vitraj/топаз.htm')
def трахит(request):
    return render(request, 'vitraj/трахит.htm')
def тремолит(request):
    return render(request, 'vitraj/тремолит.htm')
def турмалин(request):
    return render(request, 'vitraj/турмалин.htm')
def тюрингит(request):
    return render(request, 'vitraj/тюрингит.htm')
def уваровит(request):
    return render(request, 'vitraj/уваровит.htm')
def улексит(request):
    return render(request, 'vitraj/улексит.htm')
def фенакит(request):
    return render(request, 'vitraj/фенакит.htm')
def филлит(request):
    return render(request, 'vitraj/филлит.htm')
def флогопит(request):
    return render(request, 'vitraj/флогопит.htm')
def флюорит(request):
    return render(request, 'vitraj/флюорит.htm')
def фуксит(request):
    return render(request, 'vitraj/фуксит.htm')
def халцедон(request):
    return render(request, 'vitraj/халцедон.htm')
def халькантит(request):
    return render(request, 'vitraj/халькантит.htm')
def халькозин(request):
    return render(request, 'vitraj/халькозин.htm')
def халькопирит(request):
    return render(request, 'vitraj/халькопирит.htm')
def хлоантит(request):
    return render(request, 'vitraj/хлоантит.htm')
def хлорит(request):
    return render(request, 'vitraj/хлорит.htm')
def хлоритовый_сланец(request):
    return render(request, 'vitraj/хлоритовый_сланец.htm')
def хризоберилл(request):
    return render(request, 'vitraj/хризоберилл.htm')
def хризоколла(request):
    return render(request, 'vitraj/хризоколла.htm')
def хризопраз(request):
    return render(request, 'vitraj/хризопраз.htm')
def хризотиласбест(request):
    return render(request, 'vitraj/хризотиласбест.htm')
def хромит(request):
    return render(request, 'vitraj/хромит.htm')
def целестин(request):
    return render(request, 'vitraj/целестин.htm')
def церуссит(request):
    return render(request, 'vitraj/церуссит.htm')
def цинкит(request):
    return render(request, 'vitraj/цинкит.htm')
def циннвальдит(request):
    return render(request, 'vitraj/циннвальдит.htm')
def циозит(request):
    return render(request, 'vitraj/циозит.htm')
def циркон(request):
    return render(request, 'vitraj/циркон.htm')
def цитрин(request):
    return render(request, 'vitraj/цитрин.htm')
def чароит(request):
    return render(request, 'vitraj/чароит.htm')
def шабазит(request):
    return render(request, 'vitraj/шабазит.htm')
def шамозит(request):
    return render(request, 'vitraj/шамозит.htm')
def шеелит(request):
    return render(request, 'vitraj/шеелит.htm')
def шерл(request):
    return render(request, 'vitraj/шерл.htm')
def шмальтин(request):
    return render(request, 'vitraj/шмальтин.htm')
def шпинель(request):
    return render(request, 'vitraj/шпинель.htm')
def эвдиалит(request):
    return render(request, 'vitraj/эвдиалит.htm')
def эвклаз(request):
    return render(request, 'vitraj/эвклаз.htm')
def эвксинит(request):
    return render(request, 'vitraj/эвксинит.htm')
def эгирин(request):
    return render(request, 'vitraj/эгирин.htm')
def энаргит(request):
    return render(request, 'vitraj/энаргит.htm')
def энстатит(request):
    return render(request, 'vitraj/энстатит.htm')
def эпидот(request):
    return render(request, 'vitraj/эпидот.htm')
def эритрин(request):
    return render(request, 'vitraj/эритрин.htm')
def янтарь(request):
    return render(request, 'vitraj/янтарь.htm')
def ярозит(request):
    return render(request, 'vitraj/ярозит.htm')
def яшма(request):
    return render(request, 'vitraj/яшма.htm')
