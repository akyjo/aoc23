gcc .\day1.c

if ($?) {
	Get-Content .\data_day1.txt | .\a.exe
} else {
	Write-Host "Compilation fail...."
}
