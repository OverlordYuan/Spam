package casia.ibasic.comsumer.run;

import org.springframework.context.support.FileSystemXmlApplicationContext;
import casia.ibasic.dubbo.service.SpamService;
import com.alibaba.fastjson.JSONObject;

public class SpamConsumer {
	
	public static void main(String[] args){
		
		FileSystemXmlApplicationContext context = new FileSystemXmlApplicationContext(
				new String[] { "consumer.xml" });
		context.start();

		SpamService service = (SpamService)context.getBean("spam");
		JSONObject obj = new JSONObject();
		obj.put("title", "//@废橙一个:恭喜王一博！一直低调努力，博得大众喜爱！《陪你到世界之巅》正在芒果TV热播，《陈情令》正在腾讯视频热播，《天天向上》相约不变，新作《有翡》敬请期待！@UNIQ-王一博");
		obj.put("content", "//@废橙一个:恭喜王一博！一直低调努力，博得大众喜爱！《陪你到世界之巅》正在芒果TV热播，《陈情令》正在腾讯视频热播，《天天向上》相约不变，新作《有翡》敬请期待！@UNIQ-王一博");
		obj.put("source", "微博");
		System.out.println(obj);
		JSONObject result = service.spam(obj);
		System.out.println(result);
	}

}
