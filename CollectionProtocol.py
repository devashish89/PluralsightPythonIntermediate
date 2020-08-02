import unittest

from sorted_set import SortedSet

class TestConstruction(unittest.TestCase):

    def test_empty(self):
        s = SortedSet([])

    def test_from_sequences(self):
        s = SortedSet([7,8,3,1])

    def test_with_duplicates(self):
        s = SortedSet([8,8,8])

    def test_with_iterable(self):
        def gen6842():
            yield 6
            yield 8
            yield 4
            yield 2

        g = gen6842()
        s = SortedSet(g)

    def test_default_empty(self):
        s= SortedSet()

class TestContainerProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedSet([6,7,3,9])

    def test_positive_contained(self):
        self.assertTrue(6 in self.s)

    def test_negative_contained(self):
        self.assertFalse(2 in self.s)

    def test_positive_not_contained(self):
        self.assertTrue(5 not in self.s)

    def test_negative_not_contained(self):
        self.assertFalse(9 not in self.s)


class TestSizedProtocol(unittest.TestCase):

    def test_empty(self):
        s = SortedSet([])
        self.assertEqual(len(s), 0)

    def test_one(self):
        s = SortedSet([1])
        self.assertEqual(len(s), 1)

    def test_ten(self):
        s = SortedSet(range(10))
        self.assertEqual(len(s), 10)

    def test_with_duplicates(self):
        s = SortedSet([5,5,5])
        self.assertEqual(len(s),1)

class TestIterableProtocol(unittest.TestCase):
    def SetUp(self):
        self.s = SortedSet([7,1,1,3,9])

    def test_iter(self):
        i = iter(SortedSet([7,1,3,9]))
        self.assertEqual( next(i ), 1)
        self.assertEqual( next( i ), 3)
        self.assertEqual( next( i ), 7)
        self.assertEqual( next( i ), 9 )
        self.assertRaises( StopIteration, lambda: next(i))

    def test_for_loop(self):
        index = 0
        expected = [1,3,7,9]

        for item in SortedSet([7,1,1,3,9]):
            self.assertEqual(item, expected[index])
            index += 1


class TestIndexingAndSlicing(unittest.TestCase):

    def SetUp(self):
        self.s = SortedSet([1,3,9,4,6])

        # self.s is not wotking giving me a attribute Error

    def test_index_zero(self):
        self.assertEqual(SortedSet([1,3,9,4,6])[0], 1)

    def test_index_four(self):
        self.assertEqual(SortedSet([1,3,9,4,6])[4], 9)

    def test_IndexError(self):
        with self.assertRaises(IndexError):
            SortedSet([1,3,9,4,6])[5]

    def test_index_minus_one(self):
        self.assertEqual(SortedSet([1,3,9,4,6])[-1], 9)

    def test_index_minus_five(self):
        self.assertEqual(SortedSet([1,3,9,4,6])[-5], 1)

    def test_index_minus_six(self):
        with self.assertRaises(IndexError):
            SortedSet([1,3,9,4,6])[-6]

    def test_slicing_case1(self):
        self.assertEqual( SortedSet( [1, 3, 9, 4, 6] )[:], [1, 3, 4, 6, 9] )

    def test_slicing_case2(self):
        self.assertEqual( SortedSet( [1, 3, 9, 4, 6] )[:2], [1, 3] )

    def test_slicing_case3(self):
        self.assertEqual( SortedSet( [1, 3, 9, 4, 6] )[2:3], [4] )

    def test_slicing_case4(self):
        self.assertEqual( SortedSet( [1, 3, 9, 4, 6] )[4:], [9] )


class TestReprMethod(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(repr(SortedSet()), "SortedSet([])")

    def test_case2(self):
        self.assertEqual(repr(SortedSet([1,2,3])), "SortedSet([1, 2, 3])")


class TestEquality(unittest.TestCase):

    def test_case1(self):
        self.assertTrue(SortedSet([1,2,3]) == [1,2,3])

    def test_case2(self):
        self.assertFalse(SortedSet([1,2,3]) == SortedSet([1,2,3]))

    def test_case2(self):
        self.assertTrue(SortedSet([1,2,3]) != SortedSet([2,3,4]))

    def test_case2(self):
        self.assertTrue(SortedSet([1,2,3]) != [2,3,4])


class TestReversed(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(reversed(SortedSet([1,2,3])), [3,2,1])

    def test_case2(self):
        self.assertEqual(reversed(SortedSet([])), [])

    def test_case3(self):
        self.assertEqual(reversed(SortedSet()), [])

class Test_Index_Method(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(SortedSet( [1, 3, 9, 4, 6]).index(3), 1)

    def test_case2(self):
        with self.assertRaises(ValueError):
            SortedSet([1,2,3]).index(10)


class TestCaseCountMethod(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(SortedSet([1, 3, 9, 4, 6]).count(3), 1)

    def test_case2(self):
        self.assertEqual(SortedSet([]).count(3), 0)


class TestConcatenate(unittest.TestCase):

    def test_case1(self):
        s1 = SortedSet([1,2,3])
        s2 = SortedSet([4,5,5,6])
        self.assertEqual(s1+s2, [1,2,3,4,5,6])

    def test_case2(self):
        s1 = SortedSet( [1, 2, 3] )
        s2 = SortedSet( [3, 4, 5] )
        self.assertEqual( s1 + s2, [1, 2, 3, 4, 5])


class TestMultiplier(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(SortedSet([1,2,3,3])*0, [1, 2, 3])

    def test_case2(self):
        self.assertEqual(SortedSet([1,2,3,3])*3, [1, 2, 3, 1, 2, 3, 1, 2, 3])

class Test_SetMethods(unittest.TestCase):

    def test_union(self):
        s1 = SortedSet([1, 2, 3])
        s2 = SortedSet([1, 2, 3, 4, 8])
        self.assertEqual(s1.union(s2), {1,2,3,4,8})

    def test_intersection(self):
        s1 = SortedSet([1, 2, 3])
        s2 = SortedSet([1, 2, 3, 4, 8])
        self.assertEqual(s1.intersection(s2), {1,2,3})

    def test_symmetricdifference(self):
        s1 = SortedSet([1, 2, 3])
        s2 = SortedSet([2, 3, 4, 8])
        self.assertEqual(s1.symmetric_difference(s2), {1, 4, 8})

    def test_difference(self):
        s1 = SortedSet( [1, 2, 3] )
        s2 = SortedSet( [2, 3, 4, 8] )
        self.assertEqual( s1.difference( s2 ), {1})


    def test_isdisjoint(self):
        s1 = SortedSet( [1, 2, 3] )
        s2 = SortedSet( [4, 8] )
        self.assertTrue(s1.isdisjoint(s2))




if __name__ == "__main__":
    unittest.main()