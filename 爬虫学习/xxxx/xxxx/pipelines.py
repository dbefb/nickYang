# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from xxxx.items import juQingItem,xiJuItem,dongZuoItem,aiQingItem,keHuanItem,dongHuaItem,xuanYiItem,jinSongItem,kongBuItem,jiLuItem,duanPianItem,qingSeItem,tongXingItem,yinYueItem,geWuItem,jiaTingItem,erTongItem,zhuanJiItem,liShiItem,zhanZhenItem,fanZuiItem,xiBuItem,qiHuanItem,maoXianItem,zaiNanItem,wuXiaItem,guZhuangItem,yunDongItem,heiSeItem

class XxxxPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, juQingItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣剧情电影排行榜.txt','a+')
            f.writelines(['\n',data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n',])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
               
            f.close
            return item
        if isinstance(item, xiJuItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣喜剧电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item, dongZuoItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣动作电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item, aiQingItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣爱情电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item, keHuanItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣科幻电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item, dongHuaItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣动画电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item, xuanYiItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣悬疑电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item, jinSongItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣惊悚电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item, kongBuItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣恐怖电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item, jiLuItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣记录电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item, duanPianItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣短片电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item, qingSeItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣情色电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item, tongXingItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣同性电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item, yinYueItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣音乐电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item, geWuItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣歌舞电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item, jiaTingItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣家庭电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item, erTongItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣儿童电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item, zhuanJiItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣传记电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item, liShiItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣历史电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item, zhanZhenItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣战争电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item,fanZuiItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣犯罪电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item, xiBuItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣西部电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item, qiHuanItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣奇幻电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item, maoXianItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣冒险电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item, zaiNanItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣灾难电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item, wuXiaItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣武侠电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item, guZhuangItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣古装电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item, yunDongItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣运动电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        if isinstance(item, heiSeItem):
            data=item
            f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣黑色电影排行榜.txt','a+')
            f.writelines([data['filmName'],' ','评分:',data['scores'],' ','排名:',str(data['rank']),'\n'])
            if data['href']=='无连接':
                f.writelines(['无链接'])
                f.writelines(['\n'])
            else:
                weishu=int(data['weishu'])
                f.writelines(['可观看的连接，其中包含付费和免费的:','\n'])
                f.writelines([data['href'],'\n'])
                for x in range(2,weishu+1):
                    f.writelines([data['href'+str(x)],'\n'])
            f.close
            return item
        
