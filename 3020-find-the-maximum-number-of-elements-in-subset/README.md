# 3020. Find the Maximum Number of Elements in Subset

A subset forms the pattern [x, x², x⁴, ..., x², x], so for each base value we greedily chain x → x² → x⁴... while each level appears at least twice, adding 2 per level. If the peak value exists in the array we add 1, else subtract 1 (the last pair is invalid). The value 1 is special: count its odd occurrences. Track the max.
