def solution(skill, skill_trees):
    answer = 0
    skillList = list(skill)
    for i in range(len(skill_trees)):
        for j in range(0,len(skillList)):
            if skillList[0] in skill_trees[i]:
                if len(skillList) == 1 :
                    answer += 1
                    break

                if skill_trees.index(skillList[j-1]) < skill_trees.index(skillList[j]):
                    continue
                else :
                    break

                if j == len(skillList)-1 and skill_trees.index(skillList[j-1]) < skill_trees.index(skillList[j]):
                    answer += 1
                    break
                else:
                    break



        for j in range(len(skillList)):
            if skillList[j] not in skill_trees[i]:
                continue
            else:
                break
            if j == len(skillList-1) and skillList[j] not in skill_trees[i]:
                answer += 1
            else:
                break




    return answer
print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))
