package casia.ibasic.dubbo.impl;

import casia.ibasic.dubbo.service.SpamService;
import com.alibaba.fastjson.JSONObject;
import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.EntityUtils;
import org.apache.http.impl.client.HttpClients;
import org.apache.log4j.Logger;
import java.util.*;

/**
 * 垃圾过滤组件实现类
 * @author Overlord.Y
 * @version 1.0 2019年10月09日
 * @since jdk1.8
 */
public class SpamServiceImpl implements SpamService {
	private static final Logger logger = Logger.getLogger(SpamServiceImpl.class.getName());

	public JSONObject spam(JSONObject data) {
		JSONObject o = new JSONObject();
		try {
			if (null == data) {
				o.put("Error", "ERROR! Empty Json Object");
				return o;
			} else {
				try {
					String url = "http://192.168.10.121:6000/SpamText_Recognition";
					HttpPost post = new HttpPost(url);
					List<NameValuePair> urlParameters = new LinkedList<NameValuePair>();
					urlParameters.add(new BasicNameValuePair("title", data.getString("title")));
					urlParameters.add(new BasicNameValuePair("content", data.getString("content")));
					urlParameters.add(new BasicNameValuePair("source", data.getString("source")));

					UrlEncodedFormEntity formEntity = new UrlEncodedFormEntity(urlParameters, "utf-8");
					post.setEntity(formEntity);

					HttpClient client = HttpClients.createDefault();
					HttpResponse response = client.execute(post);

					HttpEntity httpEntity = response.getEntity();

					o = JSONObject.parseObject(EntityUtils.toString(httpEntity, "utf-8"));
				} catch (Exception var1) {
					logger.error("Exception", var1);
					o.put("Error", "ERROR! " + var1.getMessage());
				}
			}
		} catch (Exception var2) {
			logger.error("Exception", var2);
		}
		return o;
	}

	public static void main(String[] args) {
		JSONObject obj = new JSONObject();
		SpamService service = new SpamServiceImpl();
//		long start = System.currentTimeMillis();
		try {
			long start = System.currentTimeMillis();
			String title = "沪指逼近3000点 卧龙地产再次领涨地产股" ;
			String content ="原标题：沪指逼近3000点 卧龙地产再次领涨地产股 来源：中国网地产\n" +
					"\n" +
					"中国网地产讯 19日，受到外围消息刺激，早盘沪深两市小幅高开，随后指数出现分化，沪指全天窄幅震荡，而创业板指一路震荡上扬，盘中一度涨近2%。\n" +
					"\n" +
					"从板块指数方面看，旅沪指逼近3000点 卧龙地产再次领涨地产股游、国产芯片和PCB等板块涨幅居前，石油、天然气和黄金等板块跌幅居前。\n" +
					"\n" +
					"截止收盘，沪指涨0.46%，报收2999点，再度逼近3000点；深成指涨1.01%，报收9852点；创业板指涨1.57%，报收1705点。沪股通全天净流入7.86亿元，深股通全天净流入26.3亿元。\n" +
					"\n" +
					"地产股涨幅方面，78只地产股收涨。卧龙地产领涨地产股，涨幅为6.92%，每股收报5.25元，成交额9762万元，嘉凯城、广宇发展涨幅超2%；云南城投、新湖中宝、香江控股、阳光城等均报收涨。\n" +
					"\n" +
					"跌幅方面，41只地产股收跌。其中浙江广厦跌幅最高，达到7.69%，每股收报5.28元，成交额3.72亿元。新城控股跌幅1.69%，每股收报26.24元，成交额6.04亿元；上实发展、万科A、招商蛇口、迪马股份等小幅收跌。\n" +
					"\n" +
					"换手率方面，哈高科换手率高达11.35%，每股收报10.35元，成交额4.16亿元；浙江广厦换手率高达8.02%。";
			String source="网站";
			obj.put("title", title);
			obj.put("content", content);
			obj.put("source", source);
			JSONObject result =service.spam(obj);
			System.out.println(result);
			long end = System.currentTimeMillis();
			System.out.println("Time elapse: " + (end - start) + "ms.");
		} catch (Exception var10) {
			var10.printStackTrace();
		}

		}

	}


