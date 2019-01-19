#R Exercise BA
#Notwendige Pakete laden
require("RPostgreSQL")
require("ggplot2") 

#Datenbankverbindung einrichten
pw <- {"Passwort123"} 
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, dbname = "BA",
                 host = "localhost", port = 5432,
                 user = "postgres", password = pw
				 )
				 
#Abfragen ob alle Tabellen existieren
				 
if (dbExistsTable(con, "Student") && dbExistsTable(con, "Klausur") && dbExistsTable(con, "Notenliste") == FALSE)
{print("Necessary tables are missing please check the database ")}else {print("All tables exist")}



#1. Alle Noten eines bestimmten Studierenden:

marks_of <- function(student) {
data <- dbGetQuery(con, paste("SELECT \"Note\", \"pNr\" FROM \"Notenliste\" WHERE \"matNr\" =", student)) #SQL-Statement mit übergebenem Parameter erzeugen und ausführen
if (dim(data)[1] == 0){return( paste("No result for Student:",student))} #Prüfen ob Daten vorhanden sind, falls nicht Warnung ausgeben 
else {return(data)} #Noten des Studierenden zurrück geben 
}


#2. Notenschnitt eines Studierenden

avg_marks_of <- function(student) {
data <- dbGetQuery(con, paste("SELECT \"Note\" FROM \"Notenliste\" WHERE \"matNr\" =", student)) #SQL-Statement mit übergebenem Parameter erzeugen und ausführen
if (dim(data)[1] == 0){return( paste("No result for Student:",student))} #Prüfen ob Daten vorhanden sind, falls nicht Warnung ausgeben
else {return(mean(data$Note))} #Durchschnittsnote berechnen und zurrück geben 
}


#3. Alle Noten einer Prüfung

result_of <- function(exam) {
data <- dbGetQuery(con, paste("SELECT \"Note\", \"matNr\" FROM \"Notenliste\" WHERE \"pNr\" =", exam)) #SQL-Statement mit übergebenem Parameter erzeugen und ausführen
if (dim(data)[1] == 0){return( paste("No result for Exam:",exam))} #Prüfen ob Daten vorhanden sind, falls nicht Warnung ausgeben
else {return(data)} #Noten der  Prüfung zurrück geben 
}


#4. Notenschnitt einer Prüfung

avg_result_of <- function(exam) {
data <- dbGetQuery(con, paste("SELECT \"Note\" FROM \"Notenliste\" WHERE \"pNr\" =", exam)) #SQL-Statement mit übergebenem Parameter erzeugen und ausführen
if (dim(data)[1] == 0){return( paste("No result for Exam:",exam))} #Prüfen ob Daten vorhanden sind, falls nicht Warnung ausgeben
else {return(mean(data$Note))} #Notenschnitt der Prpfung berechnen und zurrück geben 
}


#5. Notenschnitte aller Studierenden

avg_marks_all <- function() {
data <- dbGetQuery(con, paste("SELECT AVG(\"Note\"), \"matNr\" FROM \"Notenliste\" GROUP BY \"matNr\"")) #SQL-Statement erzeugen und ausführen
if (dim(data)[1] == 0){return( paste("There are no students in the database"))} #Prüfen ob Daten vorhanden sind, falls nicht Warnung ausgeben
else {return(data)} # Durchschnittsnoten der Studierenden zurrück geben 
}

#6. Meadian der Notenschnitte

med_marks_all <- function() {
data <- dbGetQuery(con, paste("SELECT AVG(\"Note\"), \"matNr\" FROM \"Notenliste\" GROUP BY \"matNr\"")) #SQL-Statement erzeugen und ausführen
if (dim(data)[1] == 0){return( paste("There are no students in the database"))} #Prüfen ob Daten vorhanden sind, falls nicht Warnung ausgeben
else {return(median(data$avg))} #Median der Noten berechnen und zurrück geben 
}

#7. Standartabweichung der Notenschnitte

stdev_marks_all  <- function() {
data <- dbGetQuery(con, paste("SELECT AVG(\"Note\"), \"matNr\" FROM \"Notenliste\" GROUP BY \"matNr\"")) #SQL-Statement erzeugen und ausführen
if (dim(data)[1] == 0){return( paste("There are no students in the database"))} #Prüfen ob Daten vorhanden sind, falls nicht Warnung ausgeben
else {return(sd(data$avg))} # Standartabweichung der Noten berechnen und zurrück geben
}

#8. Diagrammme :

#8.1 Noten einer Prüfung
result_of_graph <- function(exam) {
data <- dbGetQuery(con, paste("SELECT \"Note\", \"matNr\" FROM \"Notenliste\" WHERE \"pNr\" =", exam))  #SQL-Statement mit übergebenem Parameter erzeugen und ausführen
if (dim(data)[1] == 0){return( paste("There are no results for exam ",exam,". No visualization possible"))} #Prüfen ob Daten vorhanden sind, falls nicht Warnung ausgeben
else {ggplot(data, aes(x=Note)) + geom_histogram(color = "black", fill = "blue", bins = 13)  + labs(title=paste("Noten der Prüfung ", + exam)) +
  labs(x="Note", y="Anzahl")}  # Histogramm zeichnen
}
#8.2 Notenschnitte aller Studierenden

avg_marks_all_graph <- function() {
data <- dbGetQuery(con, paste("SELECT AVG(\"Note\"), \"matNr\" FROM \"Notenliste\" GROUP BY \"matNr\""))  #SQL-Statement mit übergebenem Parameter erzeugen und ausführen
if (dim(data)[1] == 0){return( paste("There are no students in the database. No visualization possible"))} #Prüfen ob Daten vorhanden sind, falls nicht Warnung ausgeben
else {ggplot(data, aes(x=avg)) + geom_histogram(color = "black", fill = "blue", bins = 13)  + labs(title="Durchschnittsnoten aller Studierender") +
  labs(x="Note", y="Anzahl")}  # Histogramm zeichnen
}


