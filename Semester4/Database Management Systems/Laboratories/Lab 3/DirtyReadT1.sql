USE CloudGaming
GO

SELECT * FROM Users

BEGIN TRANSACTION
UPDATE Users SET Country='Romania'
WHERE Uid = 91
WAITFOR DELAY '00:00:10'
ROLLBACK TRANSACTION