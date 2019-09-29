class Test{
static void set(int x){
    x = 100;
}
public static void main(String[] args){
    int x;
    x = 10;
    set(x);
    
    System.out.println(x);
}
}