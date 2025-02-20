-- 코드를 입력하세요
-- 코드를 입력하세요
-- 1. ANIMAL_INS (테이블) : 보호소에 들어온 동물 정보
-- ANIMAL_ID (동물 ID), ANIMAL_TYPE (생물 종), DATETIME (보호 시작일)
-- , INTAKE_CONDITION (보호 시작 시 상태), NAME (이름), SEX_UPON_INTAKE (성별 및 중성화 여부)

-- 2. ANIMAL_OUTS (테이블) : 보호소에서 나간 동물 정보
-- ANIMAL_ID (동물 ID), ANIMAL_TYPE (생물 종), DATETIME (입양일)
-- , NAME (이름), SEX_UPON_INTAKE (성별 및 중성화 여부)
# ANIMAL_OUTS의 ANIMAL_ID는 ANIMAL_INS의 ANIMAL_ID 외래 키이다.

-- 문제
# 아직 입양을 못 간 동물 중 가장 오래 보호소에 있었던 동물 3마리의 NAME과
# ANIMAL_INS.DATETIME을 조회
# ANIMAL_INS.DATETIME 기준으로 오름차순 정렬

SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS I
LEFT JOIN ANIMAL_OUTS O
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.DATETIME IS NULL
ORDER BY I.DATETIME ASC
LIMIT 3
;