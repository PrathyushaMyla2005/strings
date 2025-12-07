class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # If lengths are different, cannot be isomorphic
        if len(s) != len(t):
            return False

        map_s_to_t = {}      # mapping from s → t
        used_t_chars = set() # t-characters already mapped

        for c1, c2 in zip(s, t):

            # If c1 is already mapped
            if c1 in map_s_to_t:
                # mapping must match current c2
                if map_s_to_t[c1] != c2:
                    return False
            else:
                # If c2 already used by some other char in s → invalid
                if c2 in used_t_chars:
                    return False

                # create new mapping
                map_s_to_t[c1] = c2
                used_t_chars.add(c2)

        return True
