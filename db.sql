SELECT GM.*, A.id, A.first_name || " " || A.last_name as "FullName"
FROM levelupapi_game GM
JOIN levelupapi_gamer GMR
ON GM.gamer_id = GMR.id
JOIN auth_user A 
on GMR.user_id = A.id