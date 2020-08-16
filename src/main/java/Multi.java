package main.java;

import java.math.BigDecimal;

public class Multi {


    public static void main (String... args){

        BigDecimal x = new BigDecimal("3141592653589793238462643383279502884197169399375105820974944592");
        BigDecimal y = new BigDecimal("2718281828459045235360287471352662497757247093699959574966967627");

        //BigDecimal total = new BigDecimal("2534767745696498721291598226410808420875926624404989594109011804054230420328163716811636469827804550673802278410568911221048870743264706668346786117132264407551450821426489441139772838020127634525234251586349419324977858145598895358201970734412370962180770");

        BigDecimal result = multiplication(x, y );
        System.out.println(result);

       /* if (result.equals(total)){
            System.out.println("Yeap baby!!! ");
        }*/

    }

    public static BigDecimal multiplication (BigDecimal a, BigDecimal b ){

        if (a.compareTo(BigDecimal.valueOf(10)) > 0  ||b.compareTo(BigDecimal.valueOf(10)) > 0 ){
            return a.multiply(b);
        }
        else {
            int n = Math.max(b.scale() ,a.scale() );

            if (n % 2 != 0){
                n = n + 1;
            }

            int n2 =  n/2;
            BigDecimal split = new BigDecimal(Math.pow(10, n2));

            BigDecimal x1 = a.divide(split);
            BigDecimal x0 = a.remainder(split);

            BigDecimal y1 = b.divide(split);
            BigDecimal y0 = b.remainder(split);

            BigDecimal r = new BigDecimal(Math.pow(10, n));
            BigDecimal r2 = new BigDecimal( Math.pow(10, n2));

            BigDecimal z0 = multiplication(x1, y1);
            BigDecimal z1 = multiplication(x0, y0);
            BigDecimal z3 = multiplication(x0.add(x1), y0.add(y1)).subtract(z0).subtract( z1) ;

            z0 = z0.multiply( r);
            z3 = z3.multiply(r2);

            return z0.add(z1).add(z3);

        }



    }


}
