import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.List;
//import java.io.Writer;
import java.util.StringTokenizer;



//import java.util.regex.*;
//import java.util.regex.Pattern;
//import org.apache.commons.collections4.*;
import org.apache.commons.collections4.queue.CircularFifoQueue;
import org.apache.lucene.analysis.snowball.*;
import org.tartarus.snowball.ext.PorterStemmer;



public class TextClassification{


	public void SplitFile(String read, String writeTrain, String writeTest, int sentences){

		BufferedReader reader =null;
		BufferedWriter testwriter =null;
		BufferedWriter trainwriter =null;

		try{
			reader =new BufferedReader(new FileReader(read));
			testwriter = new BufferedWriter(new OutputStreamWriter(
					new FileOutputStream(writeTest), "utf-8"));

			trainwriter = new BufferedWriter(new OutputStreamWriter(
					new FileOutputStream(writeTrain), "utf-8"));


			CircularFifoQueue<String> q =new CircularFifoQueue<String>(sentences);

			while(reader.ready()){

				String line = reader.readLine().toLowerCase();

				if(q.size()==sentences)
				{ 
					trainwriter.write(q.get(0));
					trainwriter.newLine();
				}

				q.add(line);
			}


			for(int i=0; i<sentences;i++){

				testwriter.write(q.get(i)); 
				testwriter.newLine();

			}

		}catch(FileNotFoundException e){
			System.out.println(e);
		}
		catch (IOException e){
			System.out.println(e);
		}
		finally{
			try {reader.close();} catch(IOException e) {}
			try {testwriter.close();} catch(IOException e) {}
			try {trainwriter.close();} catch(IOException e) {}
		}


	}


	public void EditFile(String read, String write){

		BufferedReader reader =null;
		BufferedWriter writer =null;
		Stopwords sw=new Stopwords();

		try{
			reader =new BufferedReader(new FileReader(read));
			writer = new BufferedWriter(new OutputStreamWriter(
					new FileOutputStream(write), "utf-8"));

			Stemmer stemmer=new Stemmer();
			String line="";

			while(reader.ready()){


				line =reader.readLine();
				StringTokenizer st = new StringTokenizer(line);
			while(st.hasMoreTokens()){
				String temp= st.nextToken();
				if(sw.isStopword(temp))
				{

				}
				else{

					    
					    if(temp.length()>0)
					    {
					    	temp=stemmer.stripAffixes(temp);
					    }
					    	writer.write(temp); //temp.replaceAll("\n", ""));
					    	writer.write(" ");
					    }
				}
				
			}
		}catch(FileNotFoundException e){
			System.out.println(e);
		}
		catch (IOException e){
			System.out.println(e);
		}
		finally{
			try {reader.close();} catch(IOException e) {}
			try {writer.close();} catch(IOException e) {}
		}


	}



	public static void main(String[] args){
		TextClassification textClassification=new TextClassification();



		String read = "C:\\Users\\ananya\\VT\\testData\\JaneAusten.txt";
		String test= "C:\\Users\\ananya\\VT\\testData\\JaneAusten-test.txt";
		String train= "C:\\Users\\ananya\\VT\\testData\\JaneAusten-train.txt";
		String newTrain= "C:\\Users\\ananya\\VT\\testData\\JaneAusten-train-new.txt";
		String newTest= "C:\\Users\\ananya\\VT\\testData\\JaneAusten-test-new.txt";

//		String read = "C:\\Users\\ananya\\VT\\testData\\SherlockHolmes.txt";
//		String train= "C:\\Users\\ananya\\VT\\testData\\SherlockHolmes-train.txt";
//		String test= "C:\\Users\\ananya\\VT\\testData\\SherlockHolmes-test.txt";
//		String newTrain= "C:\\Users\\ananya\\VT\\testData\\SherlockHolmes-train-new.txt";
//		String newTest= "C:\\Users\\ananya\\VT\\testData\\SherlockHolmes-test-new.txt";

		int sentences= Integer.parseInt(args[0]);

		textClassification.SplitFile(read, train, test,  sentences);		
		textClassification.EditFile(train,newTrain );
		textClassification.EditFile(test,newTest);

		System.out.println("done");

		//Stemming st


	}



}
