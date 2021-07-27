import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:frontend/app/app.dart';

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);

  static Page page() => const MaterialPage<void>(child: HomePage());

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Container(
          child: IconButton(
            icon: Icon(Icons.logout),
            onPressed: () {
              BlocProvider.of<AppCubit>(context).unauthenticate();
            },
          ),
        ),
      ),
    );
  }
}
