-- 코드를 작성해주세요
-- 1. ECOLI_DATA (테이블) : 대장균 정보
-- ID (대장균 ID), PARENT_ID (부모 ID), SIZE_OF_COLONY (개체 크기)
-- DIFFERENTIATION_DATE (분화 날짜), GENOTYPE (개체 형질)
# 최초의 대장균 개체 PARENT_ID는 NULL

-- 문제
# 분류명
# SIZE_OF_COLONY <= 100 : 'LOW'
# 100 < SIZE_OF_COLONY <= 1000 : 'MEDIUM'
# 1000 < SIZE_OF_COLONY : 'HIGH'
# 대장균 ID, 분류명 SIZE를 출력
# 대장균 ID로 오름차순

SELECT ID,
    CASE
        WHEN SIZE_OF_COLONY <= 100 THEN 'LOW'
        WHEN SIZE_OF_COLONY <= 1000 THEN 'MEDIUM'
        WHEN SIZE_OF_COLONY > 1000 THEN 'HIGH'
    END AS SIZE
FROM ECOLI_DATA
ORDER BY ID ASC
;