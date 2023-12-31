/*

This is a ByteXL contest solution solved using recursion.
*/
public class ByteXL {
    public static void main(String[] args) {
        int[] arr = {1,3,2,6,7};
        fun1(arr,0,1,9);

    }
    public static void fun1(int[]arr, int point, int p2, int sum){
        if (arr.length==0 || point == arr.length){
            return;
        }
        //base condition
        if (arr[point]+arr[p2]==sum){
            System.out.println(arr[point] + " "+ arr[p2]);
        }

        if(p2<=arr.length-1 && point< arr.length-2){
            if (p2<arr.length-1){
                fun1(arr, point, p2 + 1, sum);
            } else {
                fun1(arr, point+1, 0,sum);
            }
        }
    }
    //using recursion
}