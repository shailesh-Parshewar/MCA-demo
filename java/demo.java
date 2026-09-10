import java.util.*;

public class demo {
public static void main(String[] args) {
    System.out.println("Hello World");
    var list = new ArrayList<>(List.of("one", "two", "three"));

    for(var item : list.reversed()){
        System.out.println(item);
    }
};
//  hello
};