-- 코드를 입력하세요
-- 1. ANIMAL_INS (테이블) : 보호소에 들어온 동물 정보
-- ANIMAL_ID (동물 ID), ANIMAL_TYPE (생물 종), DATETIME (보호 시작일)
-- , INTAKE_CONDITION (보호 시작 시 상태), NAME (이름), SEX_UPON_INTAKE (성별 및 중성화 여부)

-- 2. ANIMAL_OUTS (테이블) : 보호소에서 나간 동물 정보
-- ANIMAL_ID (동물 ID), ANIMAL_TYPE (생물 종), DATETIME (보호 시작일)
-- , NAME (이름), SEX_UPON_INTAKE (성별 및 중성화 여부)
# ANIMAL_OUTS의 ANIMAL_ID는 ANIMAL_INS의 ANIMAL_ID 외래 키이다.
# 일부 데이터가 유실되어 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 ANIMAL_ID와 NAME 조회
# ANIMAL_ID 순으로 조회

SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_OUTS O
LEFT JOIN ANIMAL_INS I
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.ANIMAL_ID IS NULL
ORDER BY O.ANIMAL_ID ASC
;