import info.debatty.java.stringsimilarity.Jaccard;
import info.debatty.java.stringsimilarity.JaroWinkler;
import info.debatty.java.stringsimilarity.Levenshtein;
import info.debatty.java.stringsimilarity.NormalizedLevenshtein;

import java.sql.*;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

public class CalculateSim {
    public static void main(String[] args) throws ClassNotFoundException, SQLException {
        List<String> databases = new ArrayList<>();
        databases.add("UKSW_EDUCATION_RESULTS");
        databases.add("UKSW_DISABILITY_RESULTS");
        databases.add("UKSW_DIFFICULTY_AND_FAILURE_RESULTS");
        databases.add("UKSW_LANGUAGE_RESULTS");
        databases.add("UKSW_SOCIAL_ISSUES_RESULTS");
        databases.add("UKSW_CLOTHES_AND_FASHION_RESULTS");
        databases.add("UKSW_BODY_RESULTS");
        databases.add("UKSW_DANGER_RESULTS");
        databases.add("UKSW_SPORTS_OTHER_SPORTS_RESULTS");
        databases.add("UKSW_SPACE_RESULTS");
        databases.add("UKSW_TRANSPORT_BY_CAR_OR_LORRY_RESULTS");
        databases.add("UKSW_PHONES_EMAIL_AND_THE_INTERNET_RESULTS");
        databases.add("UKSW_MUSIC_RESULTS");
        databases.add("UKSW_HOLIDAYS_RESULTS");
        databases.add("UKSW_TV_RADIO_AND_NEWS_RESULTS");
        databases.add("UKSW_HEALTH_AND_FITNESS_RESULTS");
        databases.add("UKSW_GEOGRAPHY_RESULTS");
        databases.add("UKSW_FILM_AND_THEATRE_RESULTS");
        databases.add("UKSW_WEATHER_RESULTS");
        databases.add("UKSW_SPORTS_BALL_AND_RACKET_SPORTS_RESULTS");
        databases.add("UKSW_ANIMALS_RESULTS");
        databases.add("UKSW_SHOPPING_RESULTS");
        databases.add("UKSW_BIOLOGY_RESULTS");
        databases.add("UKSW_MENTAL_HEALTH_RESULTS");
        databases.add("UKSW_PLANTS_AND_TREES_RESULTS");
        databases.add("UKSW_HOUSES_AND_HOMES_RESULTS");
        databases.add("UKSW_ENGINEERING_RESULTS");
        databases.add("UKSW_HISTORY_RESULTS");
        databases.add("UKSW_DOUBT_GUESSING_AND_CERTAINTY_RESULTS");
        databases.add("UKSW_TRANSPORT_BY_WATER_RESULTS");
        databases.add("UKSW_TRANSPORT_BY_AIR_RESULTS");
        databases.add("UKSW_SUGGESTIONS_AND_ADVICE_RESULTS");
        databases.add("UKSW_SUCCESS_RESULTS");
        databases.add("UKSW_BUILDINGS_RESULTS");
        databases.add("UKSW_LAW_AND_JUSTICE_RESULTS");
        databases.add("UKSW_WAR_AND_CONFLICT_RESULTS");
        databases.add("UKSW_PERSONAL_QUALITIES_RESULTS");
        databases.add("UKSW_OPINION_AND_ARGUMENT_RESULTS");
        databases.add("UKSW_PERMISSION_AND_OBLIGATION_RESULTS");
        databases.add("UKSW_LITERATURE_AND_WRITING_RESULTS");
        databases.add("UKSW_HEALTH_PROBLEMS_RESULTS");
        databases.add("UKSW_POLITICS_RESULTS");
        databases.add("UKSW_GARDENS_RESULTS");
        databases.add("UKSW_DRINKS_RESULTS");
        databases.add("UKSW_CRIME_AND_PUNISHMENT_RESULTS");
        databases.add("UKSW_RELIGION_AND_FESTIVALS_RESULTS");
        databases.add("UKSW_BIRDS_RESULTS");
        databases.add("UKSW_COLOURS_AND_SHAPES_RESULTS");
        databases.add("UKSW_MATHS_AND_MEASUREMENT_RESULTS");
        databases.add("UKSW_GAMES_AND_TOYS_RESULTS");
        databases.add("UKSW_PEOPLE_IN_SOCIETY_RESULTS");
        databases.add("UKSW_HEALTHCARE_RESULTS");
        databases.add("UKSW_COOKING_AND_EATING_RESULTS");
        databases.add("UKSW_FARMING_RESULTS");
        databases.add("UKSW_INSECTS_WORMS_ETC_RESULTS");
        databases.add("UKSW_TRANSPORT_BY_BUS_AND_TRAIN_RESULTS");
        databases.add("UKSW_PREFERENCES_AND_DECISIONS_RESULTS");
        databases.add("UKSW_WORKING_LIFE_RESULTS");
        databases.add("UKSW_LIFE_STAGES_RESULTS");
        databases.add("UKSW_COMPUTERS_RESULTS");
        databases.add("UKSW_ART_RESULTS");
        databases.add("UKSW_BUSINESS_RESULTS");
        databases.add("UKSW_THE_ENVIRONMENT_RESULTS");
        databases.add("UKSW_DISCUSSION_AND_AGREEMENT_RESULTS");
        databases.add("UKSW_JOBS_RESULTS");
        databases.add("UKSW_SPORTS_WATER_SPORTS_RESULTS");
        databases.add("UKSW_FAMILY_AND_RELATIONSHIPS_RESULTS");
        databases.add("UKSW_FOOD_RESULTS");
        databases.add("UKSW_PHYSICS_AND_CHEMISTRY_RESULTS");
        databases.add("UKSW_APPEARANCE_RESULTS");
        databases.add("UKSW_MONEY_RESULTS");
        databases.add("UKSW_HOBBIES_RESULTS");
        databases.add("UKSW_SCIENTIFIC_RESEARCH_RESULTS");
        databases.add("UKSW_FISH_AND_SHELLFISH_RESULTS");
        databases.add("UKSW_TIME_RESULTS");
        databases.add("UKSW_FEELINGS_RESULTS");
        databases.add("UKSW_CHANGE_CAUSE_AND_EFFECT_RESULTS");
        List<String> methods = new ArrayList<>();
        methods.add("JaroWinkler");
        methods.add("Levenshtein");
        methods.add("NLevenshtein");
        methods.add("Jaccard");
        List<String> countries = new ArrayList<>();
        countries.add("Serbian");
        countries.add("Slovak");
        countries.add("Romansh");
        countries.add("Portuguese");
        countries.add("Norwegian");
        countries.add("Macedonian");
        countries.add("Latvian");
        countries.add("Georgian");
        countries.add("Italian");
        countries.add("Hungarian");
        countries.add("Croatian");
        countries.add("Irish");
        countries.add("Finnish");
        countries.add("Estonian");
        countries.add("Greek");
        countries.add("Danish");
        countries.add("Welsh");
        countries.add("Czech");
        countries.add("Bulgarian");
        countries.add("Belarusian");
        countries.add("French");
        countries.add("English");
        countries.add("Polish");
        countries.add("Spanish");
        countries.add("German");
        Jaccard jaccard = new Jaccard();
        Levenshtein levenshtein = new Levenshtein();
        NormalizedLevenshtein normalizedLevenshtein = new NormalizedLevenshtein();
        JaroWinkler jaroWinkler = new JaroWinkler();


        for (int l = 0; l < databases.size(); l++) {
            String myDriver = "com.mysql.cj.jdbc.Driver";
            String myUrl = "jdbc:mysql://localhost/" + databases.get(l);
            Class.forName(myDriver);
            Connection conn = DriverManager.getConnection(myUrl, "", "");
            conn.setAutoCommit(false);
            System.out.println(LocalDateTime.now());
            if (l > 0) {
                System.out.println(1.0 * l / databases.size());
            }
            for (int i = 0; i < countries.size(); i++) {
                for (int j = i + 1; j < countries.size(); j++) {
                    PreparedStatement preparedStatement = conn.prepareStatement("select * from "+countries.get(i)+"Vs"+countries.get(j)+";");
                    ResultSet rs = preparedStatement.executeQuery();
                    while (rs.next()){
                        for (int k = 0; k < methods.size(); k++) {
                            PreparedStatement update = conn.prepareStatement("UPDATE `"+countries.get(i)+"Vs"+countries.get(j)+"` SET `"+methods.get(k)+""+countries.get(i)+"Vs"+countries.get(j)+"` = ? WHERE `"+countries.get(i)+"Vs"+countries.get(j)+"`.`id` = ?; ");
                            switch (k){
                                case 0:{
                                    update.setDouble(1, jaroWinkler.similarity(rs.getString(countries.get(i)), rs.getString(countries.get(j))));
                                    update.setInt(2, rs.getInt("id"));
                                    break;
                                }case 1:{
                                    update.setDouble(1, levenshtein.distance(rs.getString(countries.get(i)), rs.getString(countries.get(j))));
                                    update.setInt(2, rs.getInt("id"));
                                    break;
                                }case 2:{
                                    update.setDouble(1, normalizedLevenshtein.similarity(rs.getString(countries.get(i)), rs.getString(countries.get(j))));
                                    update.setInt(2, rs.getInt("id"));
                                    break;
                                }case 3:{
                                    update.setDouble(1, jaccard.similarity(rs.getString(countries.get(i)), rs.getString(countries.get(j))));
                                    update.setInt(2, rs.getInt("id"));
                                    break;
                                }
                            }
                        }
                    }
                    conn.commit();
                }
            }
            System.out.println(LocalDateTime.now());
            conn.commit();
            conn.close();
        }
    }
}
