# DECLARE NumArray : ARRAY[1..10] OF INTEGER
# DECLARE Found : BOOL
# DECLARE SearchElement, MidPos, MidNum, HighPos, LowPos : INT

# HighPos <- len(NumArray)
# LowPos <- 1
# MidPos <- int((HighPos - LowPos) / 2)
# MidNum <- NumArray[MidPos]
# Found <- FALSE

# WHILE Found == FALSE AND LowPos <> HighPos

#     MidPos <- int((HighPos + LowPos) / 2)
#     MidNum <- NumArray[MidPos]

#     IF SearchElement == MidNum THEN
#         Found <- TRUE

#     ELSEIF SearchElement > MidNum THEN
#         LowPos <- MidPos + 1

#     ELSEIF SearchElement < MidNum THEN
#         HighPos <- MidPos - 1
 

#     ENDIF

# ENDWHILE

# IF Found == TRUE THEN
#     OUTPUT("The element is present in the array")
# ELSEIF Found == FALSE THEN
#     OUTPUT("The element is not present in the array")

