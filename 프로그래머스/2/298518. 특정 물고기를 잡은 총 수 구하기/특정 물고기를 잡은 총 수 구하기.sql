-- 코드를 작성해주세요

-- 1. FISH_INFO (테이블) : 잡은 물고기들의 정보
-- ID (잡은 물고기의 ID), FISH_TYPE(물고기의 종류(숫자)), LENGTH(잡은 물고기의 길이(cm))
-- TIME (물고기를 잡은 날짜)
# 잡은 물고기의 길이가 10cm 이하일 경우에는 LENGTH가 NULL이고 LENGTH에 NULL만 있는 경우는 없다.

-- 2. FISH_NAME_INFO (테이블) : 물고기의 이름에 대한 정보
-- FISH_TYPE (물고기의 종류(숫자)), FISH_NAME (물고기의 이름(문자))

-- 문제
# FISH_INFO 테이블에서 잡은 BASS와 SNAPPER의 수를 출력
# 컬럼명은 FISH_COUNT

SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO
WHERE FISH_TYPE IN (
    SELECT FISH_TYPE
    FROM FISH_NAME_INFO
    WHERE FISH_NAME = 'BASS'
    OR FISH_NAME = 'SNAPPER'
    )
;