SELECT S."Fiscal Year", S."Revenue or Spending", D.dept, round(sum(S.Amount),2)
FROM SAR as S
JOIN OrgGroup as O
ON S.OrgGroupID = O.OrgGroupID
JOIN Dept as D
ON S.DeptID = D.DeptID
WHERE S."Revenue or Spending" = "Spending" and O.OrgGroup = "Public Protection" and S."Fiscal Year" = "2015" and Dept = "Police"
