from bs4 import BeautifulSoup
import requests
import time

# 爬取真实网页

url = "http://www.tripadvisor.cn/Attractions-g308272-Activities-c47-Shanghai.html"
urls = ["http://www.tripadvisor.cn/Attractions-g308272-Activities-c47{}-Shanghai.html#ATTRACTION_LIST".format("-oa" + str(i) if i != 0 else "") for i in range(0,450,30)]

# 有反爬保护，图片爬去失败
def get_info(url):
    # 获得网页返回数据
    wb_data = requests.get(url)
    # 解析网页返回数据
    soup = BeautifulSoup(wb_data.text, "lxml")

    title_list = soup.select("div.property_title > a")
    img_list = soup.select("img[width='160']")
    cate_list = soup.select("div.p13n_reasoning_v2")

    for title, img, cate in zip(title_list, img_list, cate_list):
        data = {
            "title": title.get_text(),
            "img": img.get("src"),
            "cate": list(cate.stripped_strings)
        }
        print(data)

    time.sleep(3)

"""
title:
#ATTR_ENTRY_311595 > div.property_title > a
img:
<img alt="上海外滩" width="160" style="height: 160px; width: 160px;" id="lazyload_-2137880657_2" class="photo_image" height="160" src="http://ccm.ddcdn.com/ext/photo-l/0a/cc/fc/09/photo0jpg.jpg">
cate:
#FILTERED_LIST > div:nth-child(1) > div.element_wrap > div > div.p13n_reasoning_v2
"""

# 如果爬取图片失败，可以考虑从手机端爬取图片，此处选用从手机端爬取图片，虽然还是失败了（反爬= =）
def get_mobile_info(url):
    header = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4"
    }
    # 获得网页返回数据
    wb_data = requests.get(url,headers=header)
    # 解析网页返回数据
    soup = BeautifulSoup(wb_data.text, "lxml")

    title_list = soup.select("div.container.containerLLR > div.title.titleLLR > div")
    img_list = soup.select("div.thumb.thumbLLR.soThumb > img")
    cate_list = soup.select("div.container.containerLLR > div.attraction_types")

    for title, img, cate in zip(title_list, img_list, cate_list):
        data = {
            "title": title.get_text(),
            "img": img.get("src"),
            "cate": list(cate.stripped_strings)
        }
        print(data)

    time.sleep(3)


# 有反爬保护，爬取失败
def get_fav_info():
    # 模仿用户
    url_saves = "http://www.tripadvisor.cn/Saves#538168"

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Cookie": "ServerPool=C; TASSK=enc%3AAAY%2F4k%2BUzi%2Bv%2B6MJuOOGfqOC1%2BFNQAcvSoe6mBZMaKfee55JEr8LIc2r%2F90%2FGuiYTh8WeNGWLL53w8hcCM2RvbAaLio5lsl2tI0ruL2JkC41UhSHDofpR9B7ZzZP7wHqkg%3D%3D; TAUnique=%1%enc%3AHpQUnHFM464p6r8NJADPXAsXGGv%2BuDMLo6Dkn07ZG2k2jHwltRJPGQ%3D%3D; _jzqckmp=1; __gads=ID=30e7ffae8be5dc2f:T=1479094096:S=ALNI_MZ9d0dvlCBG7ULnqVPQJg1iCUrbfQ; CommercePopunder=SuppressAll*1479094946130; TAAuth2=%1%3%3A28537a1d0be918ac575edc201a5b53a5%3AAMlbuEQQU2HziHlQgtmYeCrvOkSbXrTDanN9Z%2Ffu9T3xK1cNQajMFgDsndCPeCbfkMMY4yX%2BxPzwPYBNbs%2BGoe1Cr0y3lvQTB3wZT%2BecPBMI51Fxw0tLf0kZKpTFCneOFGUejO9Yqh%2FZhP%2Fnp1iM6kGJtAYblya%2BTK7DF6mAU7pc4o%2Ftl7bbsykDUIAB0oVEa04w2tYHkModxBBnJih2CMnE2HgY3mc5HxXIju3JhW%2FJ; bdshare_firstime=1479095031329; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RVL.311595_318l459914_318l321173_318l1979494_318l308272_318l1979501_318l1196260_318*RS.1; CM=%1%HanaPersist%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CFtrSess%2C%2C-1%7CRCPers%2C%2C-1%7CHomeAPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CRCSess%2C%2C-1%7CFtrPers%2C%2C-1%7CHomeASess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7Csesscoestorem%2C%2C-1%7CCCPers%2C%2C-1%7CCCSess%2C%2C-1%7CViatorMCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CViatorMCSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C8%2C-1%7Csessamex%2C%2C-1%7Cperscoestorem%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7Cpers_rev%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TAReturnTo=%1%%2FSmartDeals-g308272-d1196260-Shanghai_World_Financial_Center-Shanghai-Hotel-Deals.html; roybatty=TNI1625!AEvlIkSRHO0fqfB63eomtci91Hep2wSvBvcFDaTxCRaSnJ7NQMcpuQ7drtof5Koz%2FaarfBhf%2BqSftZB6e3V0syWVPLE7%2F1cDjdZ9qe5rKUDkksGuzNba5gFxQahIm8V0D%2B9tJKG5S2rHzwtg10HggBqHBB4qqiOWjNiRuJ2tc4Dz%2C1; NPID=; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1479094058; Hm_lpvt_2947ca2c006be346c7a024ce1ad9c24a=1479095583; _qzja=1.1844465936.1479094058241.1479094058241.1479094058243.1479095573182.1479095582994..0.0.25.1; _qzjc=1; _qzjto=25.1.0; _jzqa=1.492781872033731300.1479094058.1479094058.1479094058.1; _jzqc=1; TASession=%1%V2ID.CA82A500246D40DCC5DA3AEFD982EE35*SQ.97*LP.%2FAttractions-g308272-Activities-c47-Shanghai%5C.html*PR.427%7C*LS.ModuleAjax*GR.31*TCPAR.69*TBR.46*EXEX.14*ABTR.71*PPRP.54*PHTB.32*FS.98*CPU.27*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.8FAFC6477CAD1266574FE1EDAF9B454C*LF.zhCN*FA.1*DF.0*MS.-1*RMS.-1*FLO.308272*TRA.true*LD.1196260; TAUD=LA-1479094064639-1*LG-1525536-2.1.F.*LD-1525537-.....; ki_t=1479094089577%3B1479094089577%3B1479095602514%3B1%3B25; ki_r="
    }

    wb_data = requests.get(url_saves, headers=header)

    soup = BeautifulSoup(wb_data.text, "lxml")

    print(soup)

    title_list = soup.select(
        "#BODYCON > div.modules-saves-single-trip-view > div > div.trip_content > div.items > div:nth-child(2) > div.info > div.location_summary > div.title > a")
    img_list = soup.select(
        "#BODYCON > div.modules-saves-single-trip-view > div > div.trip_content > div.items > div > div.info > div.thumbnail")
    meta_list = soup.select("div.poi_type_tags > a")
    addr_list = soup.select("div.address > a")

    print(title_list, img_list, meta_list, addr_list, sep="\n")

    for title, img, meta, addr in zip(title_list, img_list, meta_list, addr_list):
        data = {
            "title": title.get_text(),
            "img": img.get("style"),
            "meta": list(meta.stripped_strings),
            "addr": list(addr.stripped_strings)
        }
        print(data)


def get_all_pages_info(urls):
    for url in urls:
        try:
            get_info(url)
        except:
            pass

def get_mobile_all_pages_info(urls):
    for url in urls:
        try:
            get_mobile_info(url)
        except:
            pass



if __name__ == "__main__":
    # get_all_pages_info(urls)
    get_mobile_all_pages_info(urls)

