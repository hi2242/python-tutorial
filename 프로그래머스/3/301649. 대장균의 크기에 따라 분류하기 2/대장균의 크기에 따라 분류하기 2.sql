-- 코드를 작성해주세요

-- 1. ECOLI_DATA (테이블) : 대장균 정보
-- ID (대장균 ID), PARENT_ID (부모 ID), SIZE_OF_COLONY (개체 크기)
-- , DIFFERENTIATION_DATE (분화 날짜), GENOTYPE (개체 형질)
# 최초의 대장균 개체의 PARENT_ID는 NULL

-- 문제
# 대장균 SIZE_OF_COLONY 내림차순
# 분류명
# 상위 0% ~ 25%를 'CRITICAL'
# 상위 26% ~ 50%를 'HIGH'
# 상위 51% ~ 75%를 'MEDIUM'
# 상위 76% ~ 100%를 'LOW'
# 대장균 ID, 분류명 COLONY_NAME을 출력
# ID에 대해 오름차순
# 총 데이터의 수는 4의 배수
# 같은 사이즈의 대장균 개체가 서로 다른 이름으로 분류되는 경우는 없음

# SELECT ID, 'CRITICAL' AS COLONY_NAME
# FROM ECOLI_DATA P
# WHERE ID = ANY(
#     SELECT ID
#     FROM ECOLI_DATA C
#     ORDER BY SIZE_OF_COLONY DESC
#     LIMIT 5
#     )
# ORDER BY ID ASC
# ;

SELECT ID,
    CASE
        WHEN NTILE_RANK = 1 THEN 'CRITICAL'
        WHEN NTILE_RANK = 2 THEN 'HIGH'
        WHEN NTILE_RANK = 3 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS COLONY_NAME
FROM (
    SELECT ID, NTILE(4) OVER (ORDER BY SIZE_OF_COLONY DESC) AS NTILE_RANK
    FROM ECOLI_DATA
) RANKED_DATA
ORDER BY ID ASC
;