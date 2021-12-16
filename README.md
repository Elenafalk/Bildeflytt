# Bildeflytt

Lite program for å flytte bilder fra en lokasjon til en annen. Under flyttingen bytter bildene navn til datoen bildet ble tatt.
Formatet er YYYYMMDD_HHmmSS. Om bilder er tatt i samme sekund vil duplikater få et versjonsnavn, for eksempel 20211216_150526(3).JPG.
For øyeblikket virker kun .JPG filer - andre filer vil ikke bli flyttet eller endret på noen måte.
Programmet lager en midlertidig mappe i til-mappen. Den blir slettet igjen på slutten hvis alt har gått som det skal.
Om noe går galt vil muligens bilder ligge igjen i mappen som du kan finne inne i til-mappen du valgte. Mappen vil hete temp.
