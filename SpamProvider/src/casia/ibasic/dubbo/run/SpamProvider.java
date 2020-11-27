package casia.ibasic.dubbo.run;

import org.apache.log4j.PropertyConfigurator;
import org.springframework.context.support.FileSystemXmlApplicationContext;

import com.alibaba.dubbo.common.logger.Logger;
import com.alibaba.dubbo.common.logger.LoggerFactory;

/**
 * 垃圾过滤组件启动类
 * @author Overlord.Y
 * @version 1.0 2019年10月09日
 * @since jdk1.8
 */
public class SpamProvider {
	
	public static void main(String[] args){
		
		PropertyConfigurator.configure("config/log4j.properties");

		FileSystemXmlApplicationContext context = new FileSystemXmlApplicationContext(
				new String[] { "provider.xml" });
		context.start();		
		
		Logger logger = LoggerFactory.getLogger(SpamProvider.class);
		
		synchronized (SpamProvider.class) {
            while (true) {
                try {
                	SpamProvider.class.wait();
                	Thread.sleep(100);
                } catch (Throwable e) {
                	logger.warn(e.getMessage() + "\n" + e.getStackTrace());
                	context.close();
                }
            }
        }
	}
}
