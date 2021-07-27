import 'package:flow_builder/flow_builder.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:frontend/app/app.dart';
import 'package:frontend/home/home.dart';

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);

  static Page page() => const MaterialPage<void>(child: HomePage());

  @override
  Widget build(BuildContext context) {
    return BlocProvider(
      create: (_) => HomeCubit(),
      child: const HomePageView(),
    );
  }
}

class HomePageView extends StatelessWidget {
  const HomePageView({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('B-Prepared'),
        actions: [
          IconButton(
            icon: Icon(Icons.logout),
            onPressed: () {
              BlocProvider.of<AppCubit>(context).unauthenticate();
            },
          ),
        ],
      ),
      body: FlowBuilder<HomeStatus>(
        state: context.select((HomeCubit bloc) => bloc.state.status),
        onGeneratePages: onGenerateHomeViewPages,
      ),
      bottomNavigationBar: BottomAppBar(
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            IconButton(
              icon: Icon(Icons.home),
              onPressed: () {
                context.read<HomeCubit>().homeToggled();
              },
            ),
            IconButton(
              icon: Icon(Icons.announcement),
              onPressed: () {
                context.read<HomeCubit>().announcementsToggled();
              },
            ),
            IconButton(icon: Icon(Icons.add), onPressed: () {}),
            IconButton(
              icon: Icon(Icons.task),
              onPressed: () {
                context.read<HomeCubit>().tasksToggled();
              },
            ),
            IconButton(
              icon: Icon(Icons.settings),
              onPressed: () {
                context.read<HomeCubit>().profileToggled();
              },
            ),
          ],
        ),
      ),
    );
  }
}

class HomePageViewView extends StatelessWidget {
  const HomePageViewView({Key? key}) : super(key: key);

  static Page page() => const MaterialPage<void>(child: HomePageViewView());

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text('Home Page'),
    );
  }
}
