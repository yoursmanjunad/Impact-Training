/*
Program to Create own Stack Using Arrays.
Here, I included methods like
push()
peek()
delete()
isEmpty()
isFull()
 */
package Day_04.Class;

public class Staccks {
    public static void main(String[] args) {
        push(10);
        push(20);
        push(30);
        push(40);
        push(50);
//        push(60);
        peek();
        delete();
        isEmpty();
        peek();
        push(90);
        isFull();

    }
    static int n=-1;
    static int size = 5;
    static int top = 0;
    static int[] DS = new int[size];
    public static void push(int num){
        if(top==size){
            System.out.println("Stack Overflow");
        }else {
            DS[top]=num;
            top+=1;
            n+=1;
            System.out.println("Pushed "+DS[top-1]+" into the Stack");
        }
    }
    //Pushing element into the Stack!
    public static void peek(){
        if(top==n){
            System.out.println("Stack Underflow");
        }else{
            System.out.println(DS[n]);
        }
    }
    //Printed the top element in the stack!
    public static void delete(){
        if(top==n){
            System.out.println("Stack Underflow");
        }else {
            DS[n]=DS[n-1];
            top-=1;
            n-=1;
        }
    }
    //Method to remove element from the stack
    public static void isEmpty(){
        if(top==n){
            System.out.println("It is empty");
        }else {
            System.out.println("There are still left "+(top-n));
        }
    }
    //Method to return if Stack is empty or not
    public static void isFull(){
        if(top == n){
            System.out.println("It is Full");
        }else {
            System.out.println("Till now filled- "+top);
        }
    }
    //Method to return if stack is full
}