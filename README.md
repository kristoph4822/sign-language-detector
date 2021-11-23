# Rozpoznawanie języka migowego
 ![obraz](https://user-images.githubusercontent.com/46055596/143024280-458464c5-ac0b-4a6e-a396-f8515c882faf.png)

 ## Opis projektu
Projekt zakłada stworzenie prostej aplikacji webowej, która przy pomocy obrazku z kamerki naszego komputera na bieżąco rozpoznaje znaki alfabetu amerykańskiego języka migowego (ASL). Na ekranie wyświetlany jest bounding box wraz z wynikiem predykcji. Dodatkowo, dana litera czytana jest na głos.
 
 Aplikacja znajduje zastosowanie przede wszystkim w samodzielnej nauce języka migowego. Może również posłużyć za bazę do budowy innych aplikacji, jak na przykład tłumaczenie języka migowego na żywo podczas telekonferencji.
 
 Projekt realizowany w ramach przedmiotu: **Wprowadzenie do aplikacji i rozwiązań opartych o Sztuczną Inteligencję i Microsoft Azure**.
 
## Funkcjonalności
 * Rozpoznawanie wszystkich znaków alfabetu amerykańskiego języka migowego poza J i Z, które nie są statyczne;
 * Pobieranie klatki z obrazku kamerki komputera co dwie sekundy i zwracanie predykcji na jej podstawie;
 * Wyświetlanie bounding boxu wraz z wynikiem predykcji i prawdopodobieństwem;
 * W przypadku braku rozpoznania znaku (prawdopodobieństwo poniżej 0.5) wyświetlana jest czerwona ramka;
 * Rozpoznana litera czytana jest na głos;
 
 ## Nasz zespół
 * Krzysztof Maciejewski (https://github.com/kristoph4822)
 * Marcin Kotecki (https://github.com/MarcinKotecki)

 ## Architektura rozwiązania
 
 ## Technologie
 Model:
 * Azure Custom Vision 
 * Tensorflow

Aplikacja webowa:
 * Azure Web App
 * Flask
 * OpenCV
 
 ## Opis rozwiązania
 ### 1. Stworzenie modelu
 Model do rozpoznawania alfabetu języka migowego został wytrenowany przy użyciu Custom Vision. Do trenowania użytko trzech źródeł danych:
 * American Sign Language Letters Dataset: https://public.roboflow.com/object-detection/american-sign-language-letters/1
 * ASL Alphabet: https://www.kaggle.com/grassknoted/asl-alphabet
 * Zdjęcia zrobione samodzielnie

Pierwszy dataset zawierał ok. 1700 zdjęć wraz z annotacjami w formacie Psacal VOC. Aby wgrać zdjęcia wraz z bounding boxami od razu do Custom Vision wykorzystano: https://github.com/ProjektCustomVisionKL/pascal-voc-to-custom-vision-uploader. Drugi dataset zawierał 87000 zdjęć bez annotacji. Do treningu wybrano po 20 losowych zdjęć z tego zbioru dla każdej litery i ręcznie otagowano je w Custom Vision. Łącznie do treningu użyto około 2500 zdjęć (średnio 104 zdjęcia na każdą literę).

Przy tworzeniu modelu użyto opcji szybkiego trenowania (Quick Training) oraz domeny typu Compact, aby móc wyeksportować model. Wyeksportowany model używany jest bezpośrednio w aplikacji webowej.

### 2. Stworzenie aplikacji webowej

 
 ## Demo działania
