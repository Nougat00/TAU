import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.stream.IntStream;

class PrimeNumberTest {

    PrimeNumber primeNumber = new PrimeNumber();

    @Test
    void isPrimeIsTrue() {
        Assertions.assertTrue(primeNumber.isPrime(5));
    }

    @Test
    void isPrimeIsFalse() {
        Assertions.assertFalse(primeNumber.isPrime(6));
    }

    @Test
    void findLargestPrime() {
        Assertions.assertEquals(13, primeNumber.findLargestPrime(15));
    }

    @Test
    void findLargestPrimeReturnMinus1() {
        Assertions.assertEquals(-1, primeNumber.findLargestPrime(0));
    }

    @Test
    void printResultWhenRangeHasPrime() {
        Assertions.assertEquals("Największa liczba pierwsza w zakresie do 40 to: 37", primeNumber.printResult(40));
    }

    @Test
    void printResultWhenRangeHasNotPrime() {
        Assertions.assertEquals("W zakresie do -5 nie znaleziono liczby pierwszej.", primeNumber.printResult(-5));
    }

    @Test
    void findPrimesInRangeWithProperRange() {
        Assertions.assertArrayEquals(IntStream.of(5, 7, 11, 13).toArray(), primeNumber.findPrimesInRange(5, 15));
    }

    @Test
    void findPrimesInRangeWithoutProperRange() {
        Assertions.assertArrayEquals(new int[0], primeNumber.findPrimesInRange(15, 5));
    }

    @Test
    void findPrimesInRangeIsNotNull() {
        Assertions.assertNotNull(primeNumber.findPrimesInRange(0, 0));
    }
}