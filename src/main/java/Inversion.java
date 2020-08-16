package main.java;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Inversion {


    public static void main(String[] args) throws IOException {

        Path path = Paths.get("src/java/resources/fileTest.txt");

        var numbers  = Files.readAllLines(path).stream().mapToInt(Integer::parseInt).toArray();



    }


    private static int[] mergeSort (int [] numbers ){

        if (numbers.length == 1){
            return numbers;
        }

        //Get the middle
        var middle = Math.floorDiv(numbers.length , 2);

         arrayLeft = Arrays.spliterator(numbers, 0, middle);

        var arrayRight = Arrays.spliterator(numbers, middle, numbers.length);







    }


    private static int[] merge (int [] left, int [] right){

        int [] result = new int[left.length + right.length];
        var indexResult = 0;
        var indexLeft = 0;
        var indexRight = 0;

        while (indexLeft < left.length && indexRight < right.length) {
            if (left[indexLeft] < right[indexRight]) {
                result[indexResult] = left[indexLeft];
                indexLeft++;
            } else {
                result[indexResult] = right[indexRight];
                indexRight++;
            }
            indexResult++;
        }

        return    Arrays.spliterator(left, indexLeft, left.length) + Arrays.spliterator(right, indexRight, right.length)
    }


}
