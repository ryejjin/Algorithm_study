#같은 게 있는지,기둥과 보의 조건이 맞는지 검사 함수

#기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
#보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
#벽면을 벗어나게 기둥, 보를 설치하는 경우는 없습니다.@
#바닥에 보를 설치 하는 경우는 없습니다.@

def solution(n, build_frame):
    def is_valid_structure(x, y, a, result):
        if a == 0: # 보
            if y == 0 or [x, y-1, 0] in result or [x, y, 1] in result or [x-1, y, 1] in result:
                return True
        else: # 기둥
            if [x, y-1, 0] in result or [x+1, y-1, 0] in result or ([x-1, y, 1] in result and [x+1, y, 1] in result):
                return True
        return False

    result = []
    for x, y, a, b in build_frame:
        if b == 1: # 건물 생성
            if is_valid_structure(x, y, a, result):
                result.append([x, y, a])
        else: # 건물 제거
            result.remove([x, y, a])
            for i in result:
                xpos, ypos, stru = i
                if not is_valid_structure(xpos, ypos, stru, result):
                    result.append([x, y, a])
                    break

    answer = sorted(result)
    return answer

n = 5
build_frame = 	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n, build_frame))