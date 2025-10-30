class Solution {
    public String addBinary(String a, String b) {
        BigInteger two = BigInteger.valueOf(2);

        BigInteger xa = BigInteger.ZERO;
        for (int i = a.length() - 1, p = 0; i >= 0; --i, ++p)
            if (a.charAt(i) == '1') xa = xa.add(two.pow(p));

        BigInteger yb = BigInteger.ZERO;
        for (int j = b.length() - 1, p = 0; j >= 0; --j, ++p)
            if (b.charAt(j) == '1') yb = yb.add(two.pow(p));

        return xa.add(yb).toString(2);
    }
}