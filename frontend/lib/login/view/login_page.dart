import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:frontend/app/app.dart';

class LoginPage extends StatelessWidget {
  const LoginPage({Key? key}) : super(key: key);

  static Page page() => const MaterialPage<void>(child: LoginPage());

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Container(
          child: IconButton(
            icon: Icon(Icons.login),
            onPressed: () {
              BlocProvider.of<AppCubit>(context).authenticate();
            },
          ),
        ),
      ),
    );
  }
}
