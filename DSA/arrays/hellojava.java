public class hellojava {
    public static void main(String[] args) {
  int [] pee = {1, 2, 3, 4, 5};
  int min = pee[4]; 

  for (int i =0; i<pee.length ; i++){
        if (pee[i]<min){
            min = pee[i];

        }
    }
    System.out.println("the min number is " + min);
  
    }
}