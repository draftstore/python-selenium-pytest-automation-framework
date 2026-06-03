Add-Type -AssemblyName System.Windows.Forms

$dialog = New-Object System.Windows.Forms.OpenFileDialog
$dialog.Title = "Select an attachment image for OrangeHRM automation test"
$dialog.Filter = "Image Files (*.png;*.jpg;*.jpeg)|*.png;*.jpg;*.jpeg"
$dialog.Multiselect = $false

if ($dialog.ShowDialog() -eq "OK") {
    $destinationFolder = "test_data\attachments"

    if (!(Test-Path $destinationFolder)) {
        New-Item -ItemType Directory -Path $destinationFolder | Out-Null
    }

    $extension = [System.IO.Path]::GetExtension($dialog.FileName)
    $destinationFile = Join-Path $destinationFolder "orangehrm_attachment_test_image$extension"

    Copy-Item $dialog.FileName $destinationFile -Force

    Write-Host "Image copied successfully:" -ForegroundColor Green
    Write-Host $destinationFile -ForegroundColor Cyan
} else {
    Write-Host "No image selected." -ForegroundColor Yellow
}