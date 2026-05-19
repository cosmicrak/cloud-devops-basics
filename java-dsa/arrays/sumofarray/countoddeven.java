package sumofarray;
public class countoddeven{
    public static void main(String argd[]){
        int [] arr = {1, 2, 3, 4, 5};
        int oddcount = 0; 
        int evencount = 0;
        for (int i=0; i<arr.length; i++){
            if (arr[i] % 2 == 0){
                evencount++;
            }
            else{
                oddcount++;
            }
        }
        System.out.println("Number of odd elements: " + oddcount);
        System.out.println("Number of even elements: " + evencount);
    }
}