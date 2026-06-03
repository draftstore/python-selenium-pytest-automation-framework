Add-Type -AssemblyName System.Windows.Forms

$maxFileSizeBytes = 1MB
$allowedExtensions = @(".jpg", ".jpeg", ".png")
$destinationFolder = "test_data\attachments"

$dialog = New-Object System.Windows.Forms.OpenFileDialog
$dialog.Title = "Select JPG or PNG images below 1MB for OrangeHRM automation test"
$dialog.Filter = "Image Files (*.jpg;*.jpeg;*.png)|*.jpg;*.jpeg;*.png"
$dialog.Multiselect = $true

if ($dialog.ShowDialog() -ne "OK") {
    Write-Host "No image selected." -ForegroundColor Yellow
    Write-Host "You must select at least one JPG or PNG image to prepare attachment test data." -ForegroundColor Yellow
    exit 1
}

if (!(Test-Path $destinationFolder)) {
    New-Item -ItemType Directory -Path $destinationFolder | Out-Null
}

$successCount = 0
$failedCount = 0

foreach ($selectedFile in $dialog.FileNames) {
    $selectedFileInfo = Get-Item $selectedFile
    $extension = [System.IO.Path]::GetExtension($selectedFile).ToLower()

    Write-Host ""
    Write-Host "Processing file: $($selectedFileInfo.Name)" -ForegroundColor White

    if ($allowedExtensions -notcontains $extension) {
        Write-Host "Skipped: Invalid file type." -ForegroundColor Red
        Write-Host "Only JPG, JPEG, and PNG images are allowed." -ForegroundColor Yellow
        Write-Host "Selected file type: $extension" -ForegroundColor Cyan
        $failedCount++
        continue
    }

    if ($selectedFileInfo.Length -gt $maxFileSizeBytes) {
        Write-Host "Skipped: Image size exceeded." -ForegroundColor Red
        Write-Host "You need to select an image below 1MB because it is the website image upload requirement." -ForegroundColor Yellow
        Write-Host "Selected file size: $([math]::Round($selectedFileInfo.Length / 1MB, 2)) MB" -ForegroundColor Cyan
        $failedCount++
        continue
    }

    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $randomSuffix = Get-Random -Minimum 1000 -Maximum 9999
    $destinationFileName = "Test_Data_Image_${timestamp}_${randomSuffix}_ImageUpload$extension"
    $destinationFile = Join-Path $destinationFolder $destinationFileName

    Copy-Item $selectedFile $destinationFile -Force

    Write-Host "Image copied successfully:" -ForegroundColor Green
    Write-Host $destinationFile -ForegroundColor Cyan
    Write-Host "File type: $extension" -ForegroundColor Green
    Write-Host "File size: $([math]::Round($selectedFileInfo.Length / 1KB, 2)) KB" -ForegroundColor Green

    $successCount++
}

Write-Host ""
Write-Host "Image preparation summary:" -ForegroundColor White
Write-Host "Successful uploads to project folder: $successCount" -ForegroundColor Green
Write-Host "Skipped files: $failedCount" -ForegroundColor Yellow
Write-Host "Destination folder: $destinationFolder" -ForegroundColor Cyan