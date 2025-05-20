import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.stream.Stream;
import javax.xml.transform.Source;

public class DirectoryLister {

    public static void main(String[] args) {
        String directoryPath = "./0_arrays";
        Path dir = Paths.get(directoryPath);

        if (Files.exists(dir) && Files.isDirectory(dir)) {
            System.out.println("Contents of directory :" + directoryPath);
        } else {
            System.out.println("Path is not valid: " + directoryPath);
        }
    }
}
