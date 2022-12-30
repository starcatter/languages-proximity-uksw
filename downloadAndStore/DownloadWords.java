import de.tallerik.MySQL;
import de.tallerik.utils.Insert;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class DownloadAndStore {
    public static void main(String[] args) throws IOException {
        DownloadHtml downloadHtml = new DownloadHtml();
        List<String> urls = readFile("SourceList.txt");
        Map<String, List<String>> topicsAndWordList = downloadHtml.downloadHtml(urls);
        List<String> allWords = new ArrayList<>();
        MySQL sql = new MySQL();
        sql.setHost("127.0.0.1");
        sql.setUser("");
        sql.setPassword("");
        sql.setDb("");
        sql.setPort(3306); // Optional. Default: 3306
        sql.setDebug(false); // Optional. Default: false
        sql.connect();
        for(String topic : topicsAndWordList.keySet()){
            sql.custom("CREATE TABLE if not exists `uksw_words`.`"+topic.replace("-","_")+"_words` (  `id` INT NOT NULL AUTO_INCREMENT ,`english` TEXT NULL , `polish` TEXT NULL , `spanish` TEXT NULL , `german` TEXT NULL, PRIMARY KEY (`id`) ) ENGINE = InnoDB;");
            sql.custom("TRUNCATE `uksw_words`.`"+topic.replace("-","_")+"_words`");
            for(String word : topicsAndWordList.get(topic)){
                Insert ins = new Insert();
                ins.setTable(topic.replace("-","_")+"_words");
                ins.setColumns("english, polish, spanish, german");
                ins.setData(word, "", "","");
                sql.tableInsert(ins);
            }
            allWords.addAll(topicsAndWordList.get(topic));
        }
        System.out.println(allWords.size());
    }
    private static List<String> readFile(String fileName)
    {
        List<String> lines = new ArrayList<>();
        try
        {
            lines = Files.readAllLines(Paths.get(fileName), StandardCharsets.UTF_8);
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
        return lines;
    }
}
