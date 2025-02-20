-- 코드를 작성해주세요
-- 1. ECOLI_DATA (테이블) : 대장균들의 정보
-- ID (대장균 ID), PARENT_ID (부모 ID), SIZE_OF_COLONY (개체의 크기)
-- , DIFFERENTIATION_DAT (분화 날짜), GENOTYPE (개체의 형질)
# 최초의 대장균 개체의 PARENT_ID는 NULL

-- 문제
# 대장균 ID와 자식의 수 CHILD_COUNT를 출력
# 자식이 없다면 CHILD_COUNT는 0
# 개체의 ID에 대해 오름차순

SELECT P.ID, COUNT(C.ID) AS CHILD_COUNT
FROM ECOLI_DATA P
LEFT JOIN ECOLI_DATA C
ON P.ID = C.PARENT_ID
GROUP BY P.ID
ORDER BY P.ID ASC
;