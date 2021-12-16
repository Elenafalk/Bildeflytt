# Bildeflytt

Flytt bilder fra en lokasjon til en annen. Under flyttingen bytter bildene navn til datoen bildet ble tatt.
Formatet er YYYYMMDD_HHmmSS. Om bilder er tatt i samme sekund vil duplikater få et versjonsnavn, for eksempel 20211216_150526(3).JPG.
For øyeblikket virker kun .JPG filer - andre filer vil ikke bli flyttet eller endret på noen måte.
Programmet lager en midlertidig mappe i til-mappen. Den blir slettet igjen på slutten hvis alt har gått som det skal.
Om noe går galt vil muligens bilder ligge igjen i mappen som du kan finne inne i til-mappen du valgte. Mappen vil hete "temp".

Move images from one location to another. During the move, the images are renamed to the date they were taken.
The format is YYYYMMDD_HHmmSS. If images are taken on the same second, duplicates will get a version name, like so: 20211216_150526(3).JPG.
Currently only .JPG files are supported - other files will not be moved or changed in any way.
The program will create a temporary directory within the target directory. It will be deleted again if the process finished correctly.
If any errors occur, it is possible that images will remain in the temporary directory. You can look for it within the target directory, and it will be named "temp".

Please note that the UI is in Norwegian, while the source code is English. You should therefore be able to easily adapt it regardless of understanding Norwegian.
