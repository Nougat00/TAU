import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.stream.IntStream;

class MainTest {

    Main main = new Main();

    @Test
    void isPrimeIsTrue() {
        Assertions.assertTrue(main.isPrime(5));
    }

    @Test
    void isPrimeIsFalse() {
        Assertions.assertFalse(main.isPrime(6));
    }

    @Test
    void findLargestPrime() {
        Assertions.assertEquals(13, main.findLargestPrime(15));
    }

    @Test
    void findLargestPrimeReturnMinus1() {
        Assertions.assertEquals(-1, main.findLargestPrime(0));
    }

    @Test
    void printResultWhenRangeHasPrime() {
        Assertions.assertEquals("Największa liczba pierwsza w zakresie do 40 to: 37", main.printResult(40));
    }

    @Test
    void printResultWhenRangeHasNotPrime() {
        Assertions.assertEquals("W zakresie do -5 nie znaleziono liczby pierwszej.", main.printResult(-5));
    }

    @Test
    void findPrimesInRangeWithProperRange() {
        Assertions.assertArrayEquals(IntStream.of(5, 7, 11, 13).toArray(), main.findPrimesInRange(5, 15));
    }

    @Test
    void findPrimesInRangeWithoutProperRange() {
        Assertions.assertArrayEquals(new int[0], main.findPrimesInRange(15, 5));
    }

    @Test
    void findPrimesInRangeIsNotNull() {
        Assertions.assertNotNull(main.findPrimesInRange(0, 0));
    }
}