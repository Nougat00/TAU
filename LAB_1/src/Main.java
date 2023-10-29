import java.util.ArrayList;
import java.util.List;

public class Main {
    public boolean isPrime(int number) {
        if (number <= 1) {
            return false;
        }
        if (number <= 3) {
            return true;
        }
        if (number % 2 == 0 || number % 3 == 0) {
            return false;
        }

        for (int i = 5; i * i <= number; i += 6) {
            if (number % i == 0 || number % (i + 2) == 0) {
                return false;
            }
        }

        return true;
    }

    public int findLargestPrime(int max) {
        for (int i = max; i > 1; i--) {
            if (isPrime(i)) {
                return i;
            }
        }
        return -1;
    }

    public String printResult(int max) {
        int largestPrime = findLargestPrime(max);

        if (largestPrime != -1) {
            return "Największa liczba pierwsza w zakresie do " + max + " to: " + largestPrime;
        } else {
            return "W zakresie do " + max + " nie znaleziono liczby pierwszej.";
        }
    }

    public int[] findPrimesInRange(int start, int end) {
        List<Integer> primeNumbers = new ArrayList<>();
        for (int number = start; number <= end; number++) {
            if (isPrime(number)) {
                primeNumbers.add(number);
            }
        }
        return primeNumbers.stream().mapToInt(i->i).toArray();
    }

}