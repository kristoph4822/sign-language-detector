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
 ![obraz](https://user-images.githubusercontent.com/46055596/143025922-6540652b-9d5b-4400-8a31-c45ffe7bfd74.png)

 
 
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

Do stworzenia aplikacji webowej wykorzystany został framework Flask.
Aplikacja dostępna jest pod adresem: https://sign-language-detector.azurewebsites.net/
1. Strona internetowa wyświetla obraz z kamery użytkownika i co 2 sekundy wysyła pomniejszony obraz do backendu. 
2. Na backendzie, wykorzystując stworzony wcześniej model, wykrywane są na obrazie znaki języka migowego. 
3. Backend w odpowiedzi zwraca znak, lokalizację i pewność predykcji (jezeli nie został przekroczony minimalny próg pewności, zwracana jest pusta odpowiedź).
4. W przeglądarce na obrazie z kamery dookoła wykrytego znaku rysowana jest ramka z podpisem.
5. W przeglądarce odtwarzany jest dźwięk odpowiadający wykrytemu znakowi.

 ## Demo działania
 https://www.youtube.com/watch?v=z0eb3DWDp6a
 
 ## Cheatsheet
 Zaleca się stosować znaki w podobny sposób jak na poniższej ilustracji:
 
 ![obraz](https://user-images.githubusercontent.com/46055596/143035893-2d2d3080-0c9e-4e0e-9e2c-ed50f4617de1.png)

Źródło: https://www.dummies.com/languages/american-sign-language/signing-for-dummies-cheat-sheet/
