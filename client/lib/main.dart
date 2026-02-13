import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // Root widget
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: .fromSeed(seedColor: const Color.fromARGB(255, 75, 183, 58)),
        useMaterial3: true,

      ),
      home: const MyHomePage(title: 'CSM Model'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {


  @override
  Widget build(BuildContext context) {

    return Scaffold(
      appBar: AppBar(

        backgroundColor: Theme.of(context).colorScheme.inversePrimary,

        title: Text(widget.title),
      ),
      body: Center(

        child: Column(




          mainAxisAlignment: .center,
          children: [
            const Text("Modal pop up")

          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: ()=>{
          showModalBottomSheet<void>(
            context: context,
            builder: (BuildContext context){
              return Container(
                height: 200,
                color: const Color.fromARGB(255, 98, 255, 7),
                child: Center(
                  child: Column(
                    mainAxisAlignment: .center,
                    children: [
                      const Text('Here we go'),

                    ],
                  ),
                ),
              );
            }
          )
        },
        tooltip: 'Increment',
        child: const Icon(Icons.ac_unit_rounded),
      ),
    );
  }
}
